import cv2
import os

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Create a video capture object
video_name = 'vtest.avi'
capture = cv2.VideoCapture(video_name)

while True:
    # Read a video frame
    ret, frame = capture.read()

    # Quit
    if ret is False: break

    # Show the current frame
    cv2.imshow("Video Frame", frame)
    key = cv2.waitKey(1)

# Release the capture object
capture.release()

# Destroy all windows
cv2.destroyAllWindows()
