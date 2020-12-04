import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img = cv2.imread('simple.jpg',0)

# FAST
fast = cv2.FastFeatureDetector_create()
keypoints = fast.detect(img, None)

# Display result
img = cv2.drawKeypoints(img, keypoints, None, color=(255,0,0))

plt.imshow(img)
#plt.title('SIFT')
plt.xticks([]), plt.yticks([])
plt.show()