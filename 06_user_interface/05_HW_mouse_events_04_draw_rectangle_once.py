import numpy as np
import cv2
import random

# Settings
rows = 480
cols = 640

# Global variables
mouse_is_pressed = False
mouse_start_x = -1
mouse_start_y = -1
color = (255, 255, 255)
img_color = np.zeros((rows, cols, 3), np.uint8)
img_color_original = None

# Mouse event callback
def mouse_callback(event, x, y, flags, param):
    global mouse_is_pressed, mouse_start_x, mouse_start_y, color, img_color, img_color_original

    # Left button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # Flag on
        mouse_is_pressed = True

        # Record the mouse position
        mouse_start_x = x
        mouse_start_y = y

        # Pick a random color
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
        
        # Backup the original image
        img_color_original = img_color.copy()

    # Left button released
    elif event == cv2.EVENT_LBUTTONUP:
        # Flag off
        mouse_is_pressed = False

        # Draw a rectangle
        #cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1)

    # Mouse Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        # If the left button was pressed
        if mouse_is_pressed:
            # Copy the original image
            img_color = img_color_original.copy()

            # Draw a rectangle
            cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1)

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