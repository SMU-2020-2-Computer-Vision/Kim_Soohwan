import cv2
import os

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load an image
img_color = cv2.imread('messi5.jpg')

# Check if image loading is successful
if img_color is None:
    print('Error: No image exists')
    exit(1)

# Convert the color image to gray
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Save the gray image
cv2.imwrite('messi5_gray.jpg', img_gray)

# Display both images in each window
cv2.imshow('Color Image', img_color)
cv2.imshow('Gray Image', img_gray)
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()