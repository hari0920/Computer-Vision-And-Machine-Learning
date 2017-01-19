# getting started with videos.
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',codec, 24 , (640,480))# saves at 60fps :) only useful if you have a good camera though.

while (cap.isOpened()):
    # capture frame by frame
    ret, frame = cap.read()
    #if ret == True:
        # apply operations
    frame = cv2.flip(frame, 0)
    out.write(frame)
        #display the new frame
    cv2.imshow('upsidedown',frame)
    if cv2.waitKey(1) == ord('q'):
        break
    #else:
     #   break

cap.release()
out.release()
cv2.destroyAllWindows()
