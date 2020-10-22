import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a grayscale image
img_orig = cv2.imread('box.png', 0)

# Apply gradient filters
img_sobelX_8U = cv2.Sobel(img_orig, cv2.CV_8U, 1, 0, ksize=5)
img_sobelX_64F = cv2.Sobel(img_orig, cv2.CV_64F, 1, 0, ksize=5)

# Take absolute values and scale
img_sobelX_8U = cv2.convertScaleAbs(img_sobelX_8U)
img_sobelX_64F = cv2.convertScaleAbs(img_sobelX_64F)

# Display results
titles = ['Original', 'Sobel 8U', 'Sobel 64F']
images = [img_orig, img_sobelX_8U, img_sobelX_64F]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()