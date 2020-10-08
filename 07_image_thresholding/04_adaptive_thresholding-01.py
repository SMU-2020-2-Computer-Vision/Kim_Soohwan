import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load a grayscale image
img_gray = cv2.imread('sudoku.png', 0)

# Blur the image
img_blurred = cv2.medianBlur(img_gray, 5)
cv2.imshow('Original vs Blurred', cv2.hconcat([img_gray, img_blurred]))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Threshold the image
ret, img1 = cv2.threshold(img_blurred, 127, 255, cv2.THRESH_BINARY)
img2 = cv2.adaptiveThreshold(img_blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
img3 = cv2.adaptiveThreshold(img_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Display results
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img_blurred, img1, img2, img3]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
