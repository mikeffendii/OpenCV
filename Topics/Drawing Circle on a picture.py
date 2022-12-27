import cv2 as cv

img = cv.imread("./Pics/1.jpg")
cv.imshow("Image", img)

cv.circle(img,(250,250), 40, (0,255,0), thickness=-1)

cv.imshow("Image", img)
cv.waitKey(0)
