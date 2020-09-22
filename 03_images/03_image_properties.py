import cv2
import os

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Load an image
img = cv2.imread('messi5.jpg')

# Check if image loading is successful
if img is None:
    print('Error: No image exists')
    exit(1)

# Image properties: type
print(type(img))     # <class 'numpy.ndarray'>

# Image properties: number of dimensions
print(img.ndim)      # 3

# Image properties: matrix shape = (rows, cols, channels)
print(img.shape)     # (342, 548, 3)

# Image properties: number of pixels
print(img.size)      # 562248 = 342 x 548 x 3

# Image properties: image data type
print(img.dtype)     # uint8: image depth

# Image properties: image data type
print(img.itemsize)  # 1 byte

# Image properties: image data type
print(img.nbytes)    # 562248 = 562248 x 1