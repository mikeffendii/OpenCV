import cv2 as cv

def rescalingFrame(frame, scale=0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

Capture = cv.VideoCapture("./Videos/3.mp4")

while True:
    isTrue, frame = Capture.read()
    frame_resized = rescalingFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

Capture.release()
cv.destroyAllWindows()