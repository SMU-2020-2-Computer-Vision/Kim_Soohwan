import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a gray image
img = cv2.imread('simple.jpg', 0)

# SIFT
sift = cv2.xfeatures2d.SIFT_create()
keypoints_sift = sift.detect(img, None)
img_sift = cv2.drawKeypoints(img, keypoints_sift, None, color=(255,0,0))

# # SURF
# surf = cv2.xfeatures2d.SURF_create(50000)
# keypoints_surf = surf.detect(img, None)
# img_surf = cv2.drawKeypoints(img, keypoints_surf, None, color=(255,0,0))

# FAST
fast = cv2.FastFeatureDetector_create()
keypoints_fast = fast.detect(img, None)
img_fast = cv2.drawKeypoints(img, keypoints_fast, None, color=(255,0,0))

# ORB
orb = cv2.ORB_create()
keypoints_orb = orb.detect(img, None)
img_orb = cv2.drawKeypoints(img, keypoints_orb, None, color=(255,0,0))

# Display results
titles = ['SIFT', 'FAST', 'ORB']
images = [img_sift, img_fast, img_orb]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))    
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()