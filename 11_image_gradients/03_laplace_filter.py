import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a grayscale image
img_orig = cv2.imread('lena.jpg', 0)

# Apply gradient filters
img_sobelX = cv2.Sobel(img_orig, cv2.CV_64F, 1, 0, ksize=3)
img_sobelY = cv2.Sobel(img_orig, cv2.CV_64F, 0, 1, ksize=3)
img_laplace = cv2.Laplacian(img_orig, cv2.CV_64F, ksize=3)

# Take absolute values and scale
img_sobelX = cv2.convertScaleAbs(img_sobelX)
img_sobelY = cv2.convertScaleAbs(img_sobelY)
img_sobel = cv2.addWeighted(img_sobelX, 1, img_sobelY, 1, 0)
img_laplace = cv2.convertScaleAbs(img_laplace)

# Display results
titles = ['Original', 'Sobel', 'Laplace']
images = [img_orig, img_sobel, img_laplace]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# Display results
titles = ['Original', 'Sobel', 'Laplace']
images = [img_orig[53:123, 265:332], 
          img_sobel[53:123, 265:332], 
          img_laplace[53:123, 265:332]]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()