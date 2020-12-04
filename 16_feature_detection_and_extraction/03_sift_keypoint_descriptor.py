import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img = cv2.imread('home.jpg')

# Convert to a gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SIFT
sift = cv2.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray, None)

# Display result
img = cv2.drawKeypoints(gray, keypoints, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.imshow(img)
#plt.title('SIFT')
plt.xticks([]), plt.yticks([])
plt.show()