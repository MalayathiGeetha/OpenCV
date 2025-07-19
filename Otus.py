import cv2

# Read image in grayscale mode directly
img = cv2.imread("/home/rguktrkvalley/Pictures/noisyleaf.jpeg", cv2.IMREAD_GRAYSCALE)

# Apply Otsu's thresholding
_, thr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Show original and thresholded imag
cv2.imshow("OtsuThreshold", thr)
cv2.waitKey(0)
cv2.destroyAllWindows()
