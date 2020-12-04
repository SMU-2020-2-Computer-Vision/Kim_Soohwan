import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load gray images
img1 = cv2.imread('box.png', 0)          # queryImage
img2 = cv2.imread('box_in_scene.png', 0) # trainImage

# ORB
orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

# Brute-Force matching
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches
img3 = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=2)

plt.imshow(img3)
plt.title('ORB Features + Brute-Force Matching')
plt.xticks([]), plt.yticks([])
plt.show()