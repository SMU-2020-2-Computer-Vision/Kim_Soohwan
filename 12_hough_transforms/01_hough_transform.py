import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img_color = cv2.imread('sudoku.png')

# Convert to a gray
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Find Canny edges
img_edge = cv2.Canny(img_gray, 50, 150, apertureSize = 3)

# Find Hough lines
lines = cv2.HoughLines(img_edge, 1, np.pi/180, 200)

# Draw lines
img_lines = img_color.copy()
for i in range(len(lines)):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

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