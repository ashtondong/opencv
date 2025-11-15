import cv2 as cv

img = cv.imread('photos/cat2.jpeg')
cv.imshow('cat2', img)

def rescaleFrame(frame, scale=0.2):
    # works for images, videos, and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # only works for live videos
    capture.set(3,width)
    capture.set(4,height)

# reading videos
video_capture = cv.VideoCapture('videos/wego.mp4')
while True:
    isTrue, frame = video_capture.read()  # read frame by frame
    frame_resized = rescaleFrame(frame)
    cv.imshow('wego', frame) # show frame by frame
    cv.imshow('wego resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video_capture.release()
cv.destroyAllWindows

