import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Create a gradient image
img = np.zeros([160, 256], np.uint8)
for i in range(256):
    img[:, i] = i

# Image thresholding
thld = 127
max_v = 255
ret, img1 = cv2.threshold(img, thld, max_v, cv2.THRESH_BINARY)
ret, img2 = cv2.threshold(img, thld, max_v, cv2.THRESH_BINARY_INV)
ret, img3 = cv2.threshold(img, thld, 0,     cv2.THRESH_TRUNC)
ret, img4 = cv2.threshold(img, thld, 0,     cv2.THRESH_TOZERO)
ret, img5 = cv2.threshold(img, thld, 0,     cv2.THRESH_TOZERO_INV)

# Display results
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, img1, img2, img3, img4, img5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()