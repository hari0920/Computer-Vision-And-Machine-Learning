import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\Hariharan\\Pictures\\Camera Roll\\WIN_20170202_17_57_02_Pro.jpg")

# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(200,255,0), flags=0)
plt.imshow(img2), plt.show()