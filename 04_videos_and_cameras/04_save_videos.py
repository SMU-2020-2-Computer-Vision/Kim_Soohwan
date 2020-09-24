import os
import numpy as np
import cv2

# Get the path to the current file
cwd = os.path.dirname(os.path.abspath(__file__))

# Change the working directory
os.chdir(cwd)

# Create a video capture object
capture = cv2.VideoCapture(0)

# Define the codec 
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create a video writer object
writer = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(capture.isOpened()):
    # Read a video frame
    ret, frame = capture.read()
    
    if ret==True:
        # Write the current frame
        writer.write(frame)

        # Display the current frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
capture.release()
writer.release()
cv2.destroyAllWindows()