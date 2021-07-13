import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("messi5.jpg",cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img,cv.CV_64F, ksize = 3)   #methods to show edges in image
lap = np.uint8(np.absolute(lap))   #converting into unsigned integer

sobelX = cv.Sobel(img,cv.CV_64F,1,0)
sobelY = cv.Sobel(img,cv.CV_64F,0,1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv.bitwise_or(sobelX,sobelY)
canny = cv.Canny(img,100,200) #canny edge detection method

titles = ["image","Laplacian","sobelX" ,"sobelY" ,"sobelCombined" ,"canny"]
images = [img ,lap ,sobelX,sobelY,sobelCombined,canny]

for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


plt.show()
