import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image
img_rgb = cv2.imread('mario.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Load a template image as grayscale
template = cv2.imread('mario_coin.png', 0)
w, h = template.shape[::-1]

# Apply template matching
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Thresholding
threshold = 0.8
loc = np.where(res >= threshold)

# Draw a bounding box
img_res = img_rgb.copy()
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_res, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

# Display results
titles = ['Original', 'Template Matching']
images = [img_rgb, img_res]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))    
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()