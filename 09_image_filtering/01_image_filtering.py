import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load an image
img = cv2.imread('opencv_logo.jpg')

# Kernel
kernel = np.ones((5, 5), np.float32)/25

# Image Filtering
res = cv2.filter2D(img, -1, kernel)

# Display result
plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

plt.subplot(122)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.title('Averaging')
plt.axis('off')

plt.show()
