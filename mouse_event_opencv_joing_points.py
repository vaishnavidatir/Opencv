import numpy as np
import cv2

def click_event(event,x,y,flags,param):
     if event == cv2.EVENT_LBUTTONDOWN:
         cv2.circle(img,(x,y),3,(0,255,255),-1)
         points.append((x,y))
         if len(points)>=2:
           cv2.line(img,points[-1],points[-2],(0,0,255),10)
           cv2.imshow('image',img)





points = []
img = np.zeros([512,512,3],np.uint8)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
         
                       
