import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img = cv2.imread('fly.jpg')

# Convert to a gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SURF
surf = cv2.xfeatures2d.SURF_create(50000)
keypoints, descriptors = surf.detectAndCompute(img, None)

# Display result
img = cv2.drawKeypoints(img, keypoints, None, (255,0,0), 4)

plt.imshow(img)
#plt.title('SURF')
plt.xticks([]), plt.yticks([])
plt.show()