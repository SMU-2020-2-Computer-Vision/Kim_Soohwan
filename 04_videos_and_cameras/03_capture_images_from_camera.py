import cv2
import os

# Create a video capture object
capture = cv2.VideoCapture(0)

while True:
    # Read a video frame
    ret, frame = capture.read()

    if ret is False:
        print('Error: No image is captured!')
        break

    # Show the current frame
    cv2.imshow("Video Frame", frame)
    key = cv2.waitKey(1)

    # ESC
    if key == 27: break

    # Spacebar
    if key == 32:
        key = cv2.waitKey(0)
        if key == 27: break

# Release the capture object
capture.release()

# Destroy all windows
cv2.destroyAllWindows()
