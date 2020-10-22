import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load an image
img_orig = cv2.imread('SanFrancisco.jpg', 0)
#img_orig = cv2.imread('windows.jpg', 0)

# Convolute with proper kernels
img_sobelX = cv2.Sobel(img_orig, cv2. CV_64F, 1, 0, ksize=3)  # x
img_sobelY = cv2.Sobel(img_orig, cv2. CV_64F, 0, 1, ksize=3)  # y
img_laplace = cv2.Laplacian(img_orig, cv2.CV_64F, ksize=3)

# Display results
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y']
images = [img_orig, img_laplace, img_sobelX, img_sobelY]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()