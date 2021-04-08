# DEMO RESIZE & CROP IMAGE
import cv2

img = cv2.imread('imgs/drinking.jpeg')

imgResize = cv2.resize(img, (400, 500))

#print(imgResize.shape)

imgCropped = imgResize[100:400, 100:300]

cv2.imshow("ImageResize", imgResize)
cv2.imshow("ImageCropped", imgCropped)
cv2.waitKey(0)