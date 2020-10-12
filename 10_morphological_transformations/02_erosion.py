import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load grayscale images
img_orig = cv2.imread('j.png', 0)

index = 1
for kernel_size in [3,5,7]:
    # Display original
    plt.subplot(3, 4, index); index += 1
    plt.imshow(img_orig, 'gray')
    plt.title('Original')
    plt.axis('off')

    for iterations in [1,2,3]:
        # Kernel
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        # Erosion
        img_res = cv2.erode(img_orig, kernel, iterations=iterations)

        # Display results
        plt.subplot(3, 4, index); index += 1
        plt.imshow(img_res, 'gray')
        plt.title(str(kernel_size) + ' x ' + str(kernel_size) + ' @ ' + str(iterations))
        plt.axis('off')
plt.show()
