import cv2
from matplotlib import pyplot as plt
import numpy as np
from contours import *

def sharpenImage(img) :
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return img

img = cv2.imread("IMG_1707.JPG")

tweakedImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply a mask
sensitivity = 100
lower_white = np.array([0,0,255-sensitivity])
upper_white = np.array([255,sensitivity,255])

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_white, upper_white)
maskResult = cv2.bitwise_and(img, img, mask= mask)
tweakedMaskResult = cv2.cvtColor(maskResult, cv2.COLOR_BGR2GRAY)

tweakedMaskResult = cv2.GaussianBlur(tweakedMaskResult, (25,25), 0) #We perform an aggressive gaussian blur
tweakedMaskResult = sharpenImage(tweakedMaskResult) #we binary sharpen after the gassian blur

# Detect the contour
contour = findBiggestContour(tweakedMaskResult)
imageWithContour = tweakedImage.copy()
#rect = cv2.boundingRect(contour)
#box = cv2.boxPoints(rect)
cv2.drawContours(imageWithContour, [contour], -1, (0, 255, 0), 5)

transformedImage = perspectiveTransformContour(img, contour)

# Otsu's thresholding after Gaussian filtering
thresholding = cv2.cvtColor(transformedImage, cv2.COLOR_BGR2GRAY)
thresholding = cv2.GaussianBlur(thresholding,(5,5),0)
ret, thresholding = cv2.threshold(thresholding,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Write Image to disk
cv2.imwrite("result.jpg", cv2.cvtColor(thresholding, cv2.COLOR_GRAY2RGB))

#plot all images
figure = plt.figure()
plt.subplot(2,3,1), plt.title("Original Image"), plt.imshow(tweakedImage)
plt.subplot(2,3,2), plt.title("Masked Image"), plt.imshow(tweakedMaskResult, cmap="gray")
plt.subplot(2,3,3), plt.title("Contour Detection"), plt.imshow(imageWithContour)
plt.subplot(2,3,4), plt.title("Perspective Transform"), plt.imshow(transformedImage)
plt.subplot(2,3,5), plt.title("Otsu Thresholding"), plt.imshow(thresholding, cmap="gray")

plt.show();
