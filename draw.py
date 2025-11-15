import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# img = cv.imread('photos/cat4.jpeg')
# cv.imshow('cat', img)

# draw on blank
# 1. paint image a certain color:
# blank[200:300, 400:500] = 0,255,0 # [:] selects all pixels
# cv.imshow('green', blank)

# 2. draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)
# cv.imshow('rectangle', blank)

# 3. draw a circle
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
# cv.imshow("circle", blank)

# 4. draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('line', blank)

# 5. write text
cv.putText(blank, "hello world", (100,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)