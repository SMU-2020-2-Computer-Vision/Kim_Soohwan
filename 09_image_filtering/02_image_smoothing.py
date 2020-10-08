import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load an image
img = cv2.imread('opencv_logo.jpg')

# Blurring
res_blur = cv2.blur(img, (5, 5))

# Gaussian Blurring
res_gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Median blurring
res_median_blur = cv2.medianBlur(img, 5)

# Display results
titles = ['Original', 'Blur', 'Gaussian Blur', 'Median Blur']
images = [img, res_blur, res_gaussian_blur, res_median_blur]

for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.show()