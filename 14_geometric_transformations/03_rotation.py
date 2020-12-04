import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_orig = cv2.imread('messi5.jpg', 0)
rows,cols = img_orig.shape

# Rotation
M = cv2.getRotationMatrix2D((cols/2,rows/2), 90, 1)
img_res = cv2.warpAffine(img_orig, M, (cols,rows))

# Display results
titles = ['Original', 'Rotation']
images = [img_orig, img_res]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')    
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()