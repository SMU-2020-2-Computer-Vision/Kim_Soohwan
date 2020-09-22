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
        b = img_color.item(row, col, 0)
        g = img_color.item(row, col, 1)
        r = img_color.item(row, col, 2)

        # Convert it to gray
        gray = int(0.299*r + 0.587*g + 0.114*b)

        # Write the pixel to the gray image
        img_gray.itemset(row, col, gray)

# Convert the gray image to color
img_result = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

# Remove the ball area
for row in range(286, 332):
    for col in range(338, 390):

        # Write the pixel in the result image
        img_result.itemset(row, col, 0, 0) # b
        img_result.itemset(row, col, 1, 255) # g
        img_result.itemset(row, col, 2, 0)  # r

# Display the image
img_display = cv2.hconcat([img_color, img_result])
cv2.imshow('Access Pixels', img_display)
cv2.waitKey(0)
cv2.destroyAllWindows()
