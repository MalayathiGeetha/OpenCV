# save this as face_dataset.py

import cv2
import os

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

face_id = input('Enter user ID: ')
print("\n[INFO] Capturing face. Look at the camera and wait ...")

count = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:  # ESC to quit
        break
    elif count >= 30:
        break

print("[INFO] Done.")
cam.release()
cv2.destroyAllWindows()
