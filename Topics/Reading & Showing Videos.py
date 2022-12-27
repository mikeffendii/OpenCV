import cv2 as cv

Capture = cv.VideoCapture("./Videos/3.mp4")

while True:
    isTrue, frame = Capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

Capture.release()
cv.destroyAllWindows()