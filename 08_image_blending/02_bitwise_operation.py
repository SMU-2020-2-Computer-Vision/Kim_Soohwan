import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load two images
img_messi = cv2.imread('messi5.jpg')
img_logo = cv2.imread('opencv-logo-white.png')
cv2.imshow('Lionel Messi', img_messi)
cv2.imshow('OpenCV Logo', img_logo)
cv2.waitKey(0)

# Now create a mask of logo and create its inverse mask also
img_logo_gray = cv2.cvtColor(img_logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img_logo_gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img_logo.shape
roi = img_messi[0:rows, 0:cols]

# Take only region of logo from logo image
img_logo_fg = cv2.bitwise_and(img_logo, img_logo, mask = mask)

# Now black-out the area of logo in ROI
img_messi_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

# Put logo in ROI and modify the main image
dst = cv2.add(img_logo_fg, img_messi_bg)
img_messi[0:rows, 0:cols] = dst

# Display results
titles = ['Logo', 'Mask', 'Inverse Mask', 
          'Foreground', 'Background', 'Addition']
images = [img_logo, mask, mask_inv, 
          img_logo_fg, img_messi_bg, dst]
is_gray = [False, True, True, 
           False, False, False]

for i in range(6):
    plt.subplot(2, 3, i+1)
    if is_gray[i]: plt.imshow(images[i], 'gray')
    else:          plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.imshow('Bitwise Operation', img_messi)
cv2.waitKey(0)
cv2.destroyAllWindows()
