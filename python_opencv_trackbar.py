import numpy as np
import cv2 as cv

img = np.zeros([300,512,3],np.uint8)
cv.namedWindow('image')
def nothing(x):
    print(x)

switch = "ON :1\n OFF:0"
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('S','image',0,1,nothing)

while (1):
    cv.imshow("image",img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break


    b = cv.getTrackbarPos("B","image")
    g = cv.getTrackbarPos("G","image")
    r = cv.getTrackbarPos("R","image")
    s = cv.getTrackbarPos("S","image")


    if s == 0:
        img[:] = 0
    else:
        img[:] = [b ,g ,r]
