import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img_orig = cv2.imread('name_card.jpg')
rows, cols, ch = img_orig.shape

# Four correspondances
pts1 = np.float32([[93,169], [508,106], [616,305], [113,421]])
pts2 = np.float32([[0,0], [180,0], [180,100], [0,100]])

# Perspective Transformation
M = cv2.getPerspectiveTransform(pts1, pts2)
img_res = cv2.warpPerspective(img_orig, M, (180,100))

# Display results
titles = ['Original', 'Perspective Projection']
images = [img_orig, img_res]

for i in range(2):
    plt.subplot(1, 3, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))    
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()