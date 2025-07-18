# save this as face_train.py

import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L')  # grayscale
        img_numpy = np.array(gray_img, 'uint8')
        id = int(os.path.split(imagePath)[-1].split('.')[1])
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\
                  .detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples, ids

print("[INFO] Training faces. It will take a few seconds ...")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('data/trainer.yml')
print(f"[INFO] {len(np.unique(ids))} faces trained. Exiting ...")
