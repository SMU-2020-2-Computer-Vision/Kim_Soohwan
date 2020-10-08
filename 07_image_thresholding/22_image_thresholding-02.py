import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load a grayscale image
img_color = cv2.imread('traffic-light.jpg')
cv2.imshow('Traffic Light', img_color)
cv2.waitKey(0)

# Color Channels
img_B, img_G, img_R = cv2.split(img_color)

# Image thresholding
thld, max_v = 200, 255
ret, img_R_thld = cv2.threshold(img_R, thld, max_v, cv2.THRESH_BINARY)
ret, img_G_thld = cv2.threshold(img_G, thld, max_v, cv2.THRESH_BINARY)
ret, img_B_thld = cv2.threshold(img_B, thld, max_v, cv2.THRESH_BINARY)

# Display results
titles = ['Red','Green','Blue']
images = [img_R_thld, img_G_thld, img_B_thld]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
