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

    # OK
    if ret is True:

        # Show the current frame
        cv2.imshow("Video Frame", frame)
        key = cv2.waitKey(1)

        # ESC
        if key == 27: break

        # Spacebar
        if key == 32:
            key = cv2.waitKey(0)
            if key == 27: break

    # Repeat the video
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.open(video_name)

# Release the capture object
capture.release()

# Destroy all windows
cv2.destroyAllWindows()
