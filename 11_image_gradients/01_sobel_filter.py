import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a grayscale image
img_orig = cv2.imread('box.png', 0)
#img_orig = cv2.imread('white_circle.png', 0)

# Apply gradient filters
img_sobelX = cv2.Sobel(img_orig, cv2.CV_64F, 1, 0, ksize=5)
img_sobelY = cv2.Sobel(img_orig, cv2.CV_64F, 0, 1, ksize=5)

# Take absolute values and scale
img_sobelX = cv2.convertScaleAbs(img_sobelX)
img_sobelY = cv2.convertScaleAbs(img_sobelY)
img_sobel = cv2.addWeighted(img_sobelX, 1, img_sobelY, 1, 0)

# Display results
titles = ['Original', 'Sobel', 'Sobel X', 'Sobel Y']
images = [img_orig, img_sobel, img_sobelX, img_sobelY]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()