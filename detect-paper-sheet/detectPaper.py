import cv2
import numpy as np
from contours import *

MODE_OPENCV_IMAGE = 0
MODE_MEMORY_BUFFER = 1

def sharpenImage(img) :
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return img

def maskWhite(img) :
    # Apply a mask
    sensitivity = 100
    lower_white = np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    return cv2.bitwise_and(img, img, mask= mask)

def detectPaper(img, mode = MODE_OPENCV_IMAGE) :
    if(mode == MODE_MEMORY_BUFFER) :
        img = cv2.imdecode(img, cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1

    maskResult = maskWhite(img)

    grayMaskResult = cv2.cvtColor(maskResult, cv2.COLOR_BGR2GRAY)
    grayMaskResult = cv2.GaussianBlur(grayMaskResult, (25,25), 0) #We perform an aggressive gaussian blur
    grayMaskResult = sharpenImage(grayMaskResult) #we binary sharpen after the gassian blur

    # Detect the contour
    contour = findBiggestContour(grayMaskResult)

    transformedImage = perspectiveTransformContour(img, contour)

    # Otsu's thresholding after Gaussian filtering
    thresholding = cv2.cvtColor(transformedImage, cv2.COLOR_BGR2GRAY)
    thresholding = cv2.GaussianBlur(thresholding,(5,5),0)
    ret, thresholding = cv2.threshold(thresholding,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    if(mode == MODE_MEMORY_BUFFER) :
        return cv2.imencode(".jpg", thresholding)
    else :
        return thresholding, transformedImage, grayMaskResult, contour