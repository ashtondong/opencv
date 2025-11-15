import cv2 as cv

# reading images
# img_cat1 = cv.imread('photos/cat1.jpeg')
# cv.imshow('cat1', img_cat1)

# reading videos
video_capture = cv.VideoCapture('videos/wego.mp4')
while True:
    isTrue, frame = video_capture.read()  # read frame by frame
    cv.imshow('wego', frame) # show frame by frame

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video_capture.release()
cv.destroyAllWindows