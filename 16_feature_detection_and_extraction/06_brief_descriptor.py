import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img = cv2.imread('simple.jpg',0)

# STAR detector
star = cv2.xfeatures2d.StarDetector_create()
keypoints = star.detect(img,None)

# BRIEF descriptor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
keypoints, descriptors = brief.compute(img, keypoints)

# Display result
img = cv2.drawKeypoints(img, keypoints, None, color=(255,0,0))

plt.imshow(img)
#plt.title('STAR')
plt.xticks([]), plt.yticks([])
plt.show()