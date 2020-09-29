import os
import numpy as np
import cv2

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load a color image
img_color = cv2.imread('messi5.jpg')

# Check if image loading is successful
if img_color is None:
    print('Error: No image exists')
    exit(1)

# Get the image size
rows, cols = img_color.shape[:2]

# Create a gray image with the same size
img_gray = np.zeros((rows, cols), np.uint8)

# Iterate over the whole image
for row in range(rows):
    for col in range(cols):
        # Read the pixel from the color image
        B = img_color.item(row, col, 0)
        G = img_color.item(row, col, 1)
        R = img_color.item(row, col, 2)

        # Convert it to gray
        gray = int(0.299*R + 0.587*G + 0.114*B)

        # Write the pixel to the gray image
        img_gray.itemset(row, col, gray)

# Convert the gray image to color
img_result = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

# Remove the ball area
for row in range(286, 332):
    for col in range(338, 390):
        # Write the pixel in the result image
        img_result.itemset(row, col, 0,   0) # B
        img_result.itemset(row, col, 1, 255) # G
        img_result.itemset(row, col, 2,   0) # R
# img_result[286:331, 338:389, 0] = 0
# img_result[286:331, 338:389, 1] = 255
# img_result[286:331, 338:389, 2] = 0

# Display the image
img_display = cv2.hconcat([img_color, img_result])
cv2.imshow('Access Pixels', img_display)
cv2.waitKey(0)
cv2.destroyAllWindows()
