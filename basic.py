import cv2 as cv

img = cv.imread('photos/cat1.jpeg')
cv.imshow('cat1', img)

# gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# blur
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# dilating image
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('dilated', dilated)

# eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

# resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resize)

# cropping
cropped = img[0:200, 0:200]
cv.imshow('cropped',cropped)

cv.waitKey(0)