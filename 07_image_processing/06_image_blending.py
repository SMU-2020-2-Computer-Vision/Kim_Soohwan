import os
import numpy as np
import cv2

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load two images
img_park = cv2.imread('park.png')
img_tom = cv2.imread('tom.png')

# Blend those two images
cv2.imshow('Image Blending', cv2.hconcat([img_park, img_park, img_tom]))
cv2.waitKey(0)
for i in np.linspace(0, 1, 100):
    dst = cv2.addWeighted(img_park, 1-i, img_tom, i, 0)
    cv2.imshow('Image Blending', cv2.hconcat([img_park, dst, img_tom]))
    cv2.waitKey(30)
cv2.waitKey(0)
cv2.destroyAllWindows()