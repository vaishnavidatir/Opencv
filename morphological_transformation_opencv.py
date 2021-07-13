import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread("smarties.png",cv.IMREAD_GRAYSCALE)
_,mask = cv.threshold(img,200,255,cv.THRESH_BINARY_INV)

kernal = np.ones((5,5) , np.uint8)

dialation = cv.dilate(mask,kernal,iterations = 2)
erosion = cv.erode(mask,kernal,iterations = 1)
opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernal)
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernal)
gradient = cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernal)
tophat = cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernal)


titles = ["image","mask","dialation","erosion","opening","closing","gradient","tophat"]
images =[img,mask,dialation,erosion,opening,closing,gradient,tophat]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])

plt.show()
