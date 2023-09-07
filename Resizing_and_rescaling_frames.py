import cv2 as cv

capture = cv.VideoCapture(0)
image = cv.imread('Soc_sac.jpg')
cv.imshow('Soc_sac',image)
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

def rescaleFrame(frame, scale = 0.75):
    width =int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

def rescaleImg(img,scale):
    width =int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(img, dimensions, interpolation= cv.INTER_AREA)

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     cv.imshow('Video Resized', frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
cv.waitKey(0)