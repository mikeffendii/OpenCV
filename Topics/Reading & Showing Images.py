import cv2 as cv

## For reading and showing --Images--

img = cv.imread("./Pics/1.jpg")

cv.imshow("Watch", img)

cv.waitKey(0)