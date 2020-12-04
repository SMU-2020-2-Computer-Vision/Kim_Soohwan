import os
import cv2
import numpy as np

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_orig = cv2.imread('messi5.jpg')

# Scale-up
img_res = cv2.resize(img_orig, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Display results
cv2.imshow('Original', img_orig)
cv2.imshow('Scale-up', img_res)

# Wait for a key to be pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()