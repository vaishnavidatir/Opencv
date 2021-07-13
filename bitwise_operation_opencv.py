import numpy as np
import cv2


img = np.zeros([250,500,3],np.uint8)
img =cv2.rectangle(img,(200,0),(300,100),(255,255,255),-1)

img2 = np.full((250,500,3),255,np.uint8)
img2 = cv2.rectangle(img2,(0,0),(250,250),(0,0,0),-1)

bitAnd = cv2.bitwise_and(img,img2)
bitOr = cv2.bitwise_or(img,img2)
bitXor = cv2.bitwise_xor(img,img2)
bitNot1 = cv2.bitwise_not(img)
bitNot2 = cv2.bitwise_not(img2)


cv2.imshow("image1",img)
cv2.imshow("image2",img2)
#cv2.imshow("bitwiseand",bitAnd)
#cv2.imshow("bitwiseor",bitOr)
#cv2.imshow("bitwisexor",bitXor)
#cv2.imshow("bitwisenot1",bitNot1)
cv2.imshow("bitwisenot2",bitNot2)
