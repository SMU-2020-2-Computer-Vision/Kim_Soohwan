import cv2 as cv
import numpy as np

def do_nothing(x):
    pass

# Create a video capture object
capture = cv.VideoCapture(0)

# Create a window and trackbars
winname = 'Laplace of Image'
tbname_kernel = 'Kernel Size'
tbname_blur = 'Bluring Type'
cv.namedWindow(winname)
cv.createTrackbar(tbname_kernel, winname, 3, 15, do_nothing)
cv.createTrackbar(tbname_blur, winname, 0, 2, do_nothing)

# Infinite loop
while True:
    # Read a video frame
    ret, frame = capture.read()

    if ret is False:
        print('Error: No image is captured!')
        break

    # Convert the frame to gray
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Get the kernel size
    sigma = cv.getTrackbarPos(tbname_kernel, winname)
    ksize = (sigma*5)|1

    # Get the blurring method
    smooth_type = cv.getTrackbarPos(tbname_blur, winname)
    if smooth_type == 0:
        img_blur = cv.GaussianBlur(img_gray, (ksize, ksize), sigma, sigma)
    if smooth_type == 1:
        img_blur = cv.blur(img_gray, (ksize, ksize))
    if smooth_type == 2:
        img_blur = cv.medianBlur(img_gray, ksize)

    # Laplacian edge detection
    img_laplace = cv.Laplacian(img_blur, cv.CV_16S, 5)

    # Converting back to uint8
    img_laplace = cv.convertScaleAbs(img_laplace, (sigma+1)*0.25)

    # Display result
    cv.imshow(winname, img_laplace)
    k = cv.waitKey(5)
    if k == 27:
        break

cv.destroyAllWindows()