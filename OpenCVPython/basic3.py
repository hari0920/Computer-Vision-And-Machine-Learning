# Playing back videos
import numpy as np
import cv2

cap =cv2.VideoCapture('output.avi')

while(cap.isOpened()):
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # displays greyscale version of the video

    cv2.imshow('video',gray)
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()