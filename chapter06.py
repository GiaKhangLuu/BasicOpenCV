# JOINING IMAGE
import cv2
import numpy as np

img1 = cv2.resize(cv2.imread('imgs/khang.jpeg'), (200, 200))
img2 = cv2.resize(cv2.imread('imgs/drinking.jpeg'), (200, 200))

#imgHor = np.hstack([img1, img2])
#imgVer = np.vstack([img1, img2])
#mix = np.vstack([imgHor, imgHor])

imgGray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imgGray = np.expand_dims(imgGray, axis=2)
imgGray = np.insert(imgGray, imgGray.shape[2], 0 , axis=2)
imgGray = np.insert(imgGray, imgGray.shape[2], 0 , axis=2)
mix = np.hstack([imgGray, img2])


#cv2.imshow("Horizontal", imgHor)
#cv2.imshow("Vertical", imgVer)
cv2.imshow("Mix", mix)
cv2.waitKey(5000)
