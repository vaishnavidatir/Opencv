import numpy as np
import cv2


img = cv2.imread("messi5.jpg")
img2 = cv2.imread("orange.jpg")

print(img.shape)  #returns tuple of number of rows ,columns,channels
print(img.size)  #returns Total number of pixels
print(img.dtype) #return image datatype is obtained
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))



ball = img[280:340, 330:390]
img[273:333, 100:160] = ball


img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

#dst = cv2.add(img,img2);
dst = cv2.addWeighted(img,.2,img2,.8,0);


cv2.imshow("image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
