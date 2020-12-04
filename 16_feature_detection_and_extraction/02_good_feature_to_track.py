import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img = cv2.imread('simple.jpg')

# Convert to a gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shi-Tomasi Corner Detection
corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

# Display result
for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

plt.imshow(img)
plt.title('Good Features to Track')
plt.xticks([]), plt.yticks([])
plt.show()