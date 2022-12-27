import cv2 as cv

Capture = cv.VideoCapture(0)

while True:
    isTrue, frame = Capture.read()

    cv.imshow('Camera', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

Capture.release()
cv.destroyAllWindows()