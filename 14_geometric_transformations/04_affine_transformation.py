import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image
img_orig = cv2.imread('drawing.png')
rows,cols,ch = img_orig.shape

# Affine Transformation
pts1 = np.float32([[50,50], [200,50], [50,200]])
pts2 = np.float32([[10,100], [200,50], [100,250]])
M = cv2.getAffineTransform(pts1, pts2)
img_res = cv2.warpAffine(img_orig, M, (cols,rows))

# Display results
titles = ['Original', 'Affine Transformation']
images = [img_orig, img_res]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()