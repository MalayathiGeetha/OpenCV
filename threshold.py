import cv2
img=cv2.imread("/home/rguktrkvalley/Pictures/coin.jpeg")
img=cv2.resize(img,(600,500))

_,th=cv2.threshold(img,90,255,cv2.THRESH_BINARY)

cv2.imshow("threshold",th)
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()