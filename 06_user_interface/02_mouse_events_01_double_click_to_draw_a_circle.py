import cv2
import numpy as np
import random

# mouse callback function
def mouse_callback(event, x, y, flags, param):
    # Left button double clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Pick a random radius
        radius = random.randrange(10, 50)

        # Pick a random color
        color = (random.randrange(256), random.randrange(256), random.randrange(256))

        # Draw a circle
        cv2.circle(img_color, (x,y), radius, color,-1)

# Create a black image
rows = 480
cols = 640
img_color = np.zeros((rows, cols, 3), np.uint8)

# Create a window
winname = 'Mouse Events'
cv2.namedWindow(winname)

# Register the mouse callback function
cv2.setMouseCallback(winname, mouse_callback)

# Infinite loop
while True:
    cv2.imshow(winname, img_color)
    key = cv2.waitKey(1)
    if key == 27: break

cv2.destroyAllWindows()