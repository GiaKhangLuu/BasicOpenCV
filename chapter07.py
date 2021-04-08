# COLOR DETECTION
import cv2
import numpy as np

img = cv2.imread('imgs/khang.jpeg')
img = cv2.resize(img, (600, 600))

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def empty(a):
    hue_min = cv2.getTrackbarPos("Hue min", "TrackBar")
    hue_max = cv2.getTrackbarPos("Hue max", "TrackBar")
    sat_min = cv2.getTrackbarPos("Sat min", "TrackBar")
    sat_max = cv2.getTrackbarPos("Sat max", "TrackBar")
    val_min = cv2.getTrackbarPos("Val min", "TrackBar")
    val_max = cv2.getTrackbarPos("Val max", "TrackBar")
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)

# Create trackbar
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 300, 300)
cv2.createTrackbar("Hue min", "TrackBar", 0, 179, empty)
cv2.createTrackbar("Hue max", "TrackBar", 36, 179, empty)
cv2.createTrackbar("Sat min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Sat max", "TrackBar", 82, 255, empty)
cv2.createTrackbar("Val min", "TrackBar", 113, 255, empty)
cv2.createTrackbar("Val max", "TrackBar", 255, 255, empty)


#cv2.imshow("Image", imgHSV)
cv2.waitKey(0)
