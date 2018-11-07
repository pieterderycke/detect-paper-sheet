import cv2
from matplotlib import pyplot as plt
import numpy as np
import pytesseract
from detectPaper import *

img = cv2.imread("IMG_1608.JPG")
thresholding, transformedImage, grayMaskResult, contour = detectPaper(img)

tweakedImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Draw the Contour
imageWithContour = tweakedImage.copy()
cv2.drawContours(imageWithContour, [contour], -1, (0, 255, 0), 5)

# Write Image to disk
cv2.imwrite("result.jpg", cv2.cvtColor(thresholding, cv2.COLOR_GRAY2RGB))

# Retrieve the text
text = pytesseract.image_to_string(thresholding, lang="nld")

#plot all images
figure = plt.figure()
plt.subplot(2,3,1), plt.title("Original Image"), plt.imshow(tweakedImage)
plt.subplot(2,3,2), plt.title("Masked Image"), plt.imshow(grayMaskResult, cmap="gray")
plt.subplot(2,3,3), plt.title("Contour Detection"), plt.imshow(imageWithContour)
plt.subplot(2,3,4), plt.title("Perspective Transform"), plt.imshow(transformedImage)
plt.subplot(2,3,5), plt.title("Otsu Thresholding"), plt.imshow(thresholding, cmap="gray")

plt.show();