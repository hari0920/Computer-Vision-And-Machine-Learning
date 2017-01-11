# Getting started with images
import numpy as np
import cv2
from matplotlib import pyplot as plt
# read and display an image using matplotlib and opencv.
img = cv2.imread("C:\Users\Hariharan\Pictures\suit.jpg")
im2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # needed to account for the different colour spaces during loading.
plt.imshow(im2,interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
# creates a named window that can be resized.
cv2.namedWindow('suit', cv2.WINDOW_NORMAL)
cv2.imshow('suit', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('suitsave.png', img)
    cv2.destroyAllWindows()
