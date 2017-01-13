import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)  # define the array for the imagewith resolution

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5, cv2.LINE_AA)

# draw a rectangle
cv2.rectangle(img, (25, 50), (250, 300), (200, 200, 150), 3, cv2.LINE_AA)

# draw a circle and an ellipse
cv2.circle(img, (150, 150), 100, (0, 255, 0), 5, cv2.LINE_AA)
cv2.ellipse(img, (256, 256), (20, 200), 10, 0, 360, (0, 0, 255), -1, cv2.LINE_AA)
# draw a polygon.
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))  # False will notproduce a closed shape

# add text to the image
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

while (True):
 cv2.imshow("image", img)
 if cv2.waitKey(0) == ord('q'):
  break
