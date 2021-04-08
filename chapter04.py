# DEMO SHAPES & TEXTS O
import cv2
import numpy as np

img = np.zeros((512, 512, 3))

# Convert black image to blue
#img[:] = 100, 0, 0
#print(img)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 5)
cv2.rectangle(img, (10, 10), (200, 200), (0, 255, 255),2)
cv2.circle(img, (100,100), 50, (0, 0, 255), 3)
cv2.putText(img, "OPEN CV", (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 1)

cv2.imshow("Output", img)
cv2.waitKey(5000)
