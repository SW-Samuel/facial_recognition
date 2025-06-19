import cv2
import pickle

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

with open("labels.pickle", "rb") as f:
    labels = pickle.load(f)
    labels = {v: k for k, v in labels.items()}

webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        id_, conf = recognizer.predict(roi_gray)

        if conf >= 45 and conf <= 85:
            nome = labels[id_]
            cv2.putText(frame, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        else:
            cv2.putText(frame, "Desconhecido", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("Reconhecimento Facial", frame)

    if cv2.waitKey(20) & 0xFF == 27:  # ESC
        break

webcam.release()
cv2.destroyAllWindows()
