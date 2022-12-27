import cv2 as cv

img = cv.imread("./Pics/1.jpg")
cv.imshow("Image", img)

cv.line(img, (0,0),(250,250), (0,255,0), thickness=2)

cv.imshow("Image", img)
cv.waitKey(0)
