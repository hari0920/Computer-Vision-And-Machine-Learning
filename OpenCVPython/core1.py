#core image processing techniques
#package import
import numpy as np
import cv2

#read an image
img = cv2.imread('C:\\Users\\Hariharan\\Desktop\\tower.jpg')
pixel = img[50,50] #individual pixel
subarray = img[0:500,0:500] #based on row and column we access a sub array with all channels.
subarray1 = img[0:500,0:500,2] #Blue
 # similarly,we can access image properties like shape and size andeven data type.
print img.shape
print img.size
print img.dtype
img[:,:,2]=0; # set all redpixels as 0
#cv2.imshow('subarray', subarray1)
cv2.imshow('nored',img)
cv2.waitKey(0)