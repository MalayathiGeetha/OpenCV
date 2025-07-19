import cv2

# Load the image
img = cv2.imread('/home/rguktrkvalley/Music/boy1.jpeg')
img = cv2.resize(img, (700, 500))

crop=img[53:237,286:406]
img[53:237,406:526]=crop
img[53:237,526:646]=crop
img[53:237,166:286]=crop
img[53:237,46:166]=crop

cv2.imshow("wscube",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
