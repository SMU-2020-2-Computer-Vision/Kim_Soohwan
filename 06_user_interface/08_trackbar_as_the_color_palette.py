import numpy as np
import cv2

# Trackbar callback function
def do_nothing(x):
    pass

# Create a black image
rows = 480
cols = 640
img_color = np.zeros((rows, cols, 3), np.uint8)

# Create a window
winname = 'Trackbar as the Color Palette'
cv2.namedWindow(winname)

# Create trackbars for color change
cv2.createTrackbar('R', winname, 0, 255, do_nothing)
cv2.createTrackbar('G', winname, 0, 255, do_nothing)
cv2.createTrackbar('B', winname, 0, 255, do_nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, winname, 0, 1, do_nothing)

# Infinite loop
while True:
    # Display the color image
    cv2.imshow(winname, img_color)
    key = cv2.waitKey(1)
    if key == 27:
        break

    # Get current positions of four trackbars
    R = cv2.getTrackbarPos('R', winname)
    G = cv2.getTrackbarPos('G', winname)
    B = cv2.getTrackbarPos('B', winname)
    S = cv2.getTrackbarPos(switch, winname)

    # If the switch is off
    if S == 0:
        img_color[:] = 0 # black
    
    # else the swich if on
    else:
        img_color[:] = [B, G, R] # RGB colors

cv2.destroyAllWindows()