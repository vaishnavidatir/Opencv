import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np



img = cv.imread("opencv-logo.png")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
blur = cv.blur(img,(5,5))
gblur = cv.GaussianBlur(img,(5,5),0)
median = cv.medianBlur(img,5) #use for salt and pepper dots
bilateralFilter = cv.bilateralFilter(img,9,75,75) #(src,diameter of area,color,color) for getting sharp edge


titles = ["imgage","2D convolution ","Blur","GaussianBlur","MedialBlur","BilateralBlur"]
images = [img,dst,blur,gblur,median,bilateralFilter]

for i in range(6):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()    
