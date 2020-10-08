import numpy as np
import cv2
import random

# Settings
rows = 480
cols = 640
radius = 5

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

    # Mouse Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        # If the left button was pressed
        if mouse_is_pressed:
            # Draw a shape
            if mode == 0: 
                # Copy the original image
                img_color = img_color_original.copy()

                # Draw a rectangle
                cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1)
            elif mode == 1:
                # Copy the original image
                img_color = img_color_original.copy()

                # Draw an ellipse
                center_x = int((x+mouse_start_x)/2)
                center_y = int((y+mouse_start_y)/2)
                axis_x = abs(int((x-mouse_start_x)/2))
                axis_y = abs(int((y-mouse_start_y)/2))
                cv2.ellipse(img_color, (center_x, center_y), (axis_x, axis_y), 0, 0, 360, color, -1)
            elif mode == 2:
                # Draw a circle
                cv2.circle(img_color, (x, y), radius, color, -1)

# Create a window
winname = 'Mouse Events'
cv2.namedWindow(winname)

# Register the mouse callback function
cv2.setMouseCallback(winname, mouse_callback)

# Infinite loop
mode = 0  # 0: draw a rectangle, 1: draw an ellipse, 2: brush
while True:
    cv2.imshow(winname, img_color)
    key = cv2.waitKey(1)
    if key == ord('m'):
        mode = (mode+1)%3
    if key == 27: 
        break

cv2.destroyAllWindows()