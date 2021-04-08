# DEMO SOME BASIC FUNCTIONS
import cv2
import numpy as np

kernel = np.ones((3, 3), int)

im = cv2.imread('imgs/khang.jpeg')
imGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
imBlur = cv2.GaussianBlur(imGray, (11, 11), 0)
imCanny = cv2.Canny(imGray, 100, 100)
imDila = cv2.dilate(imCanny, kernel, iterations=3)
imEr = cv2.erode(imDila, kernel, iterations=3)

#cv2.imshow("image", im)
#cv2.imshow("Gray image", imGray)
#cv2.imshow("Blur image", imBlur)
cv2.imshow("Canny", imCanny)
cv2.imshow("Dila", imDila)
cv2.imshow("Erode", imEr)
cv2.waitKey(0)
