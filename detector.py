import cv2
import numpy as np
 
cam =cv2.VideoCapture(0)
ref = None
while cam.isOpened(): 
  _,vid =cam.read()
  try :
    dif =cv2.absdiff(vid, ref) 
    bgr =cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY) 
    blr =cv2.GaussianBlur(bgr, (5,5), 0) 
    cv2.imshow('original', vid) 
    cv2.imshow('Extracts', blr)
  except Exception as e :
    pass
  ref =vid 
  _,vid =cam.read() 
      
  if cv2.waitKey(30) ==27: 
    break 
  
cv2.destroyAllWindows() 
cam.release()  
