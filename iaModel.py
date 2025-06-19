import cv2
import os
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

labels = {}
current_id = 0
x_train = []
y_labels = []

for root, dirs, files in os.walk("imagens"):
    for file in files:
        if file.endswith("jpg") or file.endswith("png"):
            path = os.path.join(root, file)
            label = os.path.basename(root).lower()
            
            if label not in labels:
                labels[label] = current_id
                current_id += 1

            id_ = labels[label]
            image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi = image[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

with open("labels.pickle", "wb") as f:
    pickle.dump(labels, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")
