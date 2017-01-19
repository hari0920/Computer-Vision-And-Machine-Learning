#trackbar properties
#package import
import numpy as np
import cv2
def nothing(x):
    pass

#creates a black background imageand a window for display purposes.
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

#create trackbar
cv2.createTrackbar('R','image',0,255,nothing) # we specify the window and the range of representation for the trackbar and a default argument.
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

#create a switch to toggle if program runs or not.
switch = '0:OFF and 1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing) # switch is passed as a string here.

#now on to displaying
while(1):
    cv2.imshow('image',img)
    k= cv2.waitKey(1)
    if k == ord('q'):
        break
    #we must update the trackbar positions
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    #for the three color channels
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = [0] #we want a black image.
    else:
        img[:] = [b, g, r] #note the order of channels

cv2.destroyAllWindows()