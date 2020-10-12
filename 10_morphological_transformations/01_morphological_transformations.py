import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load grayscale images
img_orig  = cv2.imread('j.png',       0)
img_noise = cv2.imread('j_noise.png', 0)
img_holes = cv2.imread('j_holes.png', 0)

# Kernel for erosion and dilation
kernel = np.ones((5, 5), np.uint8)

# Erosion
res_erosion = cv2.erode(img_orig, kernel, iterations=1)

# Dilation
res_dilation = cv2.dilate(img_orig, kernel, iterations=1)

# Morphological gradient
res_gradient = cv2.morphologyEx(img_orig, cv2.MORPH_GRADIENT, kernel)

# Opening
res_opening = cv2.morphologyEx(img_noise, cv2.MORPH_OPEN, kernel)

# Closing
res_closing = cv2.morphologyEx(img_holes, cv2.MORPH_CLOSE, kernel)

# Top Hat
res_tophat = cv2.morphologyEx(img_noise, cv2.MORPH_TOPHAT, kernel)

# Back Hat
res_blackhat = cv2.morphologyEx(img_holes, cv2.MORPH_BLACKHAT, kernel)

# Display results
titles = ['Original', 'Eroson', 'Dilation', 'Gradient',
          'Original with Noise', 'Opening', 'Origianl with Holes', 'Closing',
          'Original with Noise', 'Top Hat', 'Origianl with Holes', 'Back Hat']
images = [img_orig, res_erosion, res_dilation, res_gradient,
          img_noise, res_opening, img_holes, res_closing,
          img_noise, res_tophat, img_holes, res_blackhat]

for i in range(12):
    plt.subplot(3, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
