import cv2 as cv
import numpy as np

def do_nothing(x):
    pass

# Create a video capture object
capture = cv.VideoCapture(0)

# Create a window and trackbars
winname = 'Canny Edge Detection'
cv.namedWindow(winname)
cv.createTrackbar('minVal', winname, 2000, 5000, do_nothing)
cv.createTrackbar('maxVal', winname, 4000, 5000, do_nothing)

# Infinite loop
while True:
    # Read a video frame
    ret, frame = capture.read()

    if ret is False:
        print('Error: No image is captured!')
        break

    # Convert the frame to gray
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Get the threshold values
    minVal = cv.getTrackbarPos('minVal', winname)
    maxVal = cv.getTrackbarPos('maxVal', winname)

    # Canny edge detection
    img_edge = cv.Canny(img_gray, minVal, maxVal, apertureSize=5)

    # Display result
    img_vis = frame.copy()
    img_vis = np.uint8(img_vis/2.)
    img_vis[img_edge != 0] = (0, 255, 0)
    cv.imshow(winname, img_vis)
    ch = cv.waitKey(5)
    if ch == 27:
        break

cv.destroyAllWindows()
