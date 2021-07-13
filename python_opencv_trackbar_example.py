import cv2 as cv
import numpy as np


cv.namedWindow("image")
def nothing(x):
    print(x)
switch = "color/gray"
cv.createTrackbar(switch,"image",0,1,nothing)
cv.createTrackbar("cp","image",100,400,nothing)


while(1):
    img =img = cv.imread("lena.jpg")

    pos = cv.getTrackbarPos("cp","image")
    s = cv.getTrackbarPos(switch,"image")
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(pos),(50,150),font,5,(0,255,0),5)
    
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    

   

    if  s == 0:
        pass
    else :
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    cv.imshow("image",img)

cv.destroyAllWindows()
