import cv2 as cv
import numpy as np
img = cv.imread('huhu.jpg')

# translation
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dim)

#Rotation
def Rotation(img, angle, rotPoint):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dim = (width,height)
    return cv.warpAffine(img, rotMat, dim)


cv.waitKey(0)
