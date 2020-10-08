import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Mouse event callback
def mouse_callback(event, x, y, flags, param):
    # Left button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x = %', x)
        print('y = %', y)


# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load a grayscale image
img_color = cv2.imread('traffic-light.jpg')

# Register the mouse callback function
winname = 'test'
cv2.namedWindow(winname)
cv2.setMouseCallback(winname, mouse_callback)

cv2.imshow('test', img_color)
cv2.waitKey(0)

# ROI
#traffic_light = img_color[20:340, 260:380, :]
traffic_light = img_color
img_B, img_G, img_R = cv2.split(traffic_light)
ret, img_R1 = cv2.threshold(img_R, 200, 255, cv2.THRESH_BINARY)
ret, img_G1 = cv2.threshold(img_G, 200, 255, cv2.THRESH_BINARY) 
ret, img_B1 = cv2.threshold(img_B, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('test', cv2.hconcat([img_R1, img_G1, img_B1]))
cv2.waitKey(0)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img_R1,kernel,iterations = 5)
cv2.imshow('R',img_R1)
cv2.waitKey(0)

dilation = cv2.dilate(img_R1,kernel,iterations = 5)
cv2.imshow('R',img_R1)
cv2.waitKey(0)

closing = cv2.morphologyEx(img_R1, cv2.MORPH_CLOSE, kernel)
cv2.imshow('R',img_R1)
cv2.waitKey(0)
cv2.destroyAllWindows()

circles = cv2.HoughCircles(img_R1,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(traffic_light,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(traffic_light,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',traffic_light)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Image thresholding
thld = 127
max_v = 255
ret, img1 = cv2.threshold(img, thld, max_v, cv2.THRESH_BINARY)
ret, img2 = cv2.threshold(img, thld, max_v, cv2.THRESH_BINARY_INV)
ret, img3 = cv2.threshold(img, thld, max_v, cv2.THRESH_TRUNC)
ret, img4 = cv2.threshold(img, thld, max_v, cv2.THRESH_TOZERO)
ret, img5 = cv2.threshold(img, thld, max_v, cv2.THRESH_TOZERO_INV)

# Display results
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, img1, img2, img3, img4, img5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
