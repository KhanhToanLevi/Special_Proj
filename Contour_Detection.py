import cv2 as cv

img = cv.imread('drawing.jpg')
cv.imshow('Drawing cat', img)
# Gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# Canny method
canny = cv.Canny(img, 80,150)
cv.imshow('Canny', canny)


ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


contours, hie = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} countor(s) found!')

cv.waitKey(0)