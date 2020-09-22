import cv2
import os

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load an image
img = cv2.imread('messi5.jpg')

# Check if image loading is successful
if img is None:
    print('Error: No image exists')
    exit(1)

# Set the region of interest
ROI = img[286:332, 338:390]

# Display all channels in a window
cv2.imshow('Ball', ROI)
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()