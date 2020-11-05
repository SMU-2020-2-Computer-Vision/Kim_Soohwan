import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img_color = cv2.imread('opencv-logo-white.png')

# Convert to a gray
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Blur the image
img_blur = cv2.medianBlur(img_gray, 5)

# Find Hough circles
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=25, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

# Draw circles
img_circles = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
for i in circles[0,:]:
    cv2.circle(img_circles, (i[0],i[1]), i[2], (0,255,0), 2)
    cv2.circle(img_circles, (i[0],i[1]), 2, (0,0,255), 3)

# Display results
titles = ['Original', 'Hough Circles']
images = [img_color, img_circles]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))    
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()