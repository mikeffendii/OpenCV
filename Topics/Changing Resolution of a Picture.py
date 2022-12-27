import cv2 as cv

Capture = cv.VideoCapture("./Videos/3.mp4")

def changeReso(width, height):
    Capture.set(3,width)
    Capture.set(4,height)

while True:
    isTrue, frame = Capture.read()

    cv.imshow('Picture', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

Capture.release()
cv.destroyAllWindows()