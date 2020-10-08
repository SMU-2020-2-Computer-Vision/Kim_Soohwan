import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load an image
img = cv2.imread('taj.jpg')

# Blurring
res_blur = cv2.blur(img, (5, 5))

# Gaussian Blurring
res_gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Median blurring
res_median_blur = cv2.medianBlur(img, 5)

# Bilateral filter
res_bilateral = cv2.bilateralFilter(img, 15, 75, 75) 
  
# Display results
titles = ['Original', 'Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, res_blur, res_gaussian_blur, res_median_blur, res_bilateral]

for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.show()