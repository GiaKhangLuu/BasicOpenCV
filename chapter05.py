# DEMO WRAP
import cv2
import numpy as np

img = cv2.imread('imgs/drinking.jpeg')
img = cv2.resize(img, (500, 500))

width, height = 309 - 248, 422 - 354
pts1 = np.float32([[248, 359], [309, 354], [267, 422], [336, 410]])
pts2 = np.float32([[0, 0], [0, width], [height, 0], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output", imgOutput)

def click_evt(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        cv2.putText(img, str(x) + ' ' + str(y),
                    (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        cv2.imshow("Image", img)

#cv2.imshow("Image", img)
#cv2.setMouseCallback("Image", click_evt)
cv2.waitKey(0)
#cv2.destroyAllWindows()
