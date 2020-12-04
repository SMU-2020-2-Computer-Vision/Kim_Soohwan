import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load gray images
img1 = cv2.imread('box.png', 0)          # queryImage
img2 = cv2.imread('box_in_scene.png', 0) # trainImage

# SIFT
sift = cv2.xfeatures2d.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

# Brute-Force matching
bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptors1, descriptors2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1, keypoints1, img2, keypoints2, good, None, flags=2)

plt.imshow(img3)
plt.title('SIFT Features + Brute-Force Matching (knn)')
plt.xticks([]), plt.yticks([])
plt.show()