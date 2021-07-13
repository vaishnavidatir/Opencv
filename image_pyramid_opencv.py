import cv2 as cv
import numpy as np

img = cv.imread("lena.jpg")
layer = img.copy()
gp = [layer]
#lr1 = cv.pyrDown(img)
#lr2 = cv. pyrDown(lr1)
#hr1 = cv.pyrUp(lr1)
#hr1 = cv.pyrUp(lr2)
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
   # cv.imshow(str(i),layer)

layer = gp[5]
cv.imshow("upper level Gaussian Pyramid",layer)
lp = [layer]  #code for laplacian pyramid

for i in range(5,0,-1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1],gaussian_extended)
    cv.imshow(str(i),laplacian)



#cv.imshow("image",img)
#cv.imshow("pyrDOWN 1 IMAGE ",lr1)
#cv.imshow("pyrDOWN 2 IMAGE",lr2)
#cv.imshow("pyrUp 1 IMAGE",hr1)
cv.waitKey(0)
cv.destroyAllWindows()
