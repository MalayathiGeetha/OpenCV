import cv2
import numpy as np

img=cv2.imread("/home/rguktrkvalley/Desktop/new.png")
img=cv2.resize(img,(500,500))

m=np.ones((15,15),np.int8)

er=cv2.erode(img,m,iterations=1)
di=cv2.dilate(img,m,iterations=1)
op=cv2.morphologyEx(img,cv2.MORPH_OPEN,m,iterations=1)
#cv2.imshow("ws",img)
cv2.imshow("ws",er)
#cv2.imshow("ws",di)
cv2.waitKey(0)
cv2.destroyAllWindows()