import cv2
import os

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load an image
img = cv2.imread('messi5.jpg')
print(type(img)) # <class 'numpy.ndarray'>

print(img.ndim)  

# Image properties: matrix shape
print(img.shape)

# Image properties: number of pixels
print(img.size)

# Image properties: image data type
print(img.dtype)