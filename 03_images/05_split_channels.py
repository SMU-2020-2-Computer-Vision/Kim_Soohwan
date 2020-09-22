import cv2
import os

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load an image
img_color = cv2.imread('RGB.png')

# Check if image loading is successful
if img_color is None:
    print('Error: No image exists')
    exit(1)

# Split each color channel
img_B, img_G, img_R = cv2.split(img_color)

# Merge all channels
img_merged = cv2.merge([img_B, img_G, img_R])

# Concatenate each color channel horizontally
img_split = cv2.hconcat([img_R, img_G, img_B])

# Display all channels in a window
cv2.imshow('Original Image', img_color)
cv2.imshow('Split Channels', img_split)
cv2.imshow('Merged Channels', img_merged)
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
