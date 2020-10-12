import cv2
import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure(constrained_layout=True)
rows = cols = [3, 5, 7]
spec = fig.add_gridspec(ncols=len(cols), nrows=len(rows), width_ratios=cols, height_ratios=rows)

kernel_shape = [cv2.MORPH_RECT, cv2.MORPH_CROSS, cv2.MORPH_ELLIPSE]
kernel_shape_str = ['MORPH_RECT', 'MORPH_CROSS', 'MORPH_ELLIPSE']

for r in range(len(rows)):
    for c in range(len(cols)):
        # Create a kernel
        kernel = cv2.getStructuringElement(kernel_shape[c], (cols[c], rows[r]))

        # Display results
        ax = fig.add_subplot(spec[r, c])
        plt.imshow(kernel, 'gray', vmin=0, vmax=1)
        plt.title(kernel_shape_str[c] + ' @ ' + str(rows[r]) + ' x ' + str(cols[c]))
        plt.xticks([]), plt.yticks([])
plt.show()
