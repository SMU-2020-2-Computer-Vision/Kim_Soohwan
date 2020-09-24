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

# Infinite loop
while True:

    # Display the image in a window
    cv2.imshow('Lionel Messi', img)
    
    # Wait for a key to be pressed
    key = cv2.waitKey(1)

    # Flip the image
    if key == ord('x'):
        img = cv2.flip(img, 0)
    elif key == ord('y'):
        img = cv2.flip(img, 1)
    elif key == 27:
        break

# Destroy all windows
cv2.destroyAllWindows()
