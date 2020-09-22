import cv2
import os

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load an image in a grayscale
img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)

# Check if image loading is successful
if img is None:
    print('Error: No image exists')
    exit(1)

# Display the image in a window
cv2.imshow('Lionel Messi in Grayscale', img)

# Wait for a key to be pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
