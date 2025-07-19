# save this as face_recognize.py

import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('data/trainer.yml')
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

print("[INFO] Starting face recognition... Press 'ESC' to exit.")

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x,y,w,h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        if confidence < 60:
            text = f"User {id} - {round(100 - confidence)}%"
        else:
            text = "Unknown"

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(img, text, (x+5,y-5), font, 0.8, (255,255,255), 2)

    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

print("[INFO] Exiting...")
cam.release()
cv2.destroyAllWindows()
