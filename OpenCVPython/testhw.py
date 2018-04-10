#Homework 0 for intro to CV and DIP

#Import Needed Packages numpy and OpenCV
import cv2
import numpy as np
print ("Part 1")
#Read and Show Belltower image.
img = cv2.imread('C:/Users/Hariharan/Desktop/belltower.jpg') #format is BGR since OpenCV.
img2 = np.array(img)
cv2.namedWindow('Belltower', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Belltower', img)
if cv2.waitKey(0) == ord('q'): # quit when q key is pressed
    cv2.destroyAllWindows()

## PART 2

print ("Part 2")
unity = 'hramsha'
digit_unity = [ord(c) for c in unity] # ASCII values of each letter in unity ID.
print digit_unity
[rows,cols,channels] = img.shape
print (rows,cols,channels)
# now iterate through every pixel in the image counting occurrence.
def modify(image,i,j,k):
    for row in range(i-2,i+3):
        for col in range(j-2,j+3):
            if row>0 and row<image.shape[0] and col>0 and col<image.shape[1]:
                image.itemset((row,col,k),255)


testnum = digit_unity
for digit in testnum:
    cblue = 0
    cgreen = 0
    cred = 0
    for i in range(rows):
        for j in range(cols):
             if img.item(i,j,0) == digit:
                 cblue = cblue + 1
             if img.item(i, j, 1) == digit:
                cgreen = cgreen + 1
             if img.item(i, j, 2) == digit:
                 cred = cred + 1

#counting done
    print (cblue,cgreen,cred)

print ("Part 3")
#part 3
for digit in testnum:
    for i in range(rows):
           for j in range(cols):
                if img.item(i, j, 0) == digit:
                    modify(img2, i, j, 0) #we modify the image copy and not the original
                if img.item(i, j, 1) == digit:
                    modify(img2, i, j, 1)
                if img.item(i, j, 2) == digit:
                    modify(img2, i, j, 2)

print ("Modification Done")
cv2.namedWindow('Modified', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Modified', img2) #display the modified image with signature
key = cv2.waitKey(0)
if key == ord('q'):  # quit when q key is pressed
    cv2.destroyAllWindows()
elif key == ord('s'): #save the image if s key is pressed
    cv2.imwrite('modifiedtower2.jpg', img2)
    print ("Image Saved")
    cv2.destroyAllWindows()
