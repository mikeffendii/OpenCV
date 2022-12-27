import cv2 as cv

img = cv.imread("./Pics/1.jpg")
cv.imshow("Image", img)

cv.putText(img, "Hello", (355,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv.imshow("Image", img)
cv.waitKey(0)
