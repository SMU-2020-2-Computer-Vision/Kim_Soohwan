import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load grayscale images
img_orig = cv2.imread('j.png', 0)

# Settings
kernel_sizes = [3, 5, 7]
kernel_shapes = ['RECT', 'CROSS', 'ELLIPSE']
index = 1
for size in kernel_sizes:
    # Display original
    plt.subplot(3, 4, index); index += 1
    plt.imshow(img_orig, 'gray')
    plt.title('Original')
    plt.axis('off')

    for shape in kernel_shapes:
        # Kernel
        kernel = cv2.getStructuringElement(getattr(cv2, 'MORPH_' + shape), (size, size))

        # Dilation
        img_res = cv2.dilate(img_orig, kernel, iterations=1)

        # Display results
        plt.subplot(3, 4, index); index += 1
        plt.imshow(img_res, 'gray')
        plt.title(shape + ' @ ' + str(size) + ' x ' + str(size))
        plt.axis('off')
plt.show()
