import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img_color = cv2.imread('building.jpg')

# Convert to a gray
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Find Canny edges
img_edge = cv2.Canny(img_gray, 50, 200, apertureSize = 3)

# Find Hough lines
lines = cv2.HoughLinesP(img_edge, 1, np.pi/180, 80, minLineLength=30, maxLineGap =10)

# Draw lines
img_lines = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
for i in range(len(lines)):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(img_lines, (x1,y1), (x2,y2), (0,0,255), 2)

# Display results
titles = ['Original', 'Canny Edges', 'Hough Lines']
images = [img_color, img_edge, img_lines]
is_gray = [False, True, False]

for i in range(3):
    plt.subplot(1, 3, i+1)
    if is_gray[i]: plt.imshow(images[i], 'gray')
    else:          plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))    
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()