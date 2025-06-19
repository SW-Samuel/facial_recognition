# Facial Recognition 🧑‍💻📸

This project is a simple implementation of **Facial Recognition** using Python.

It allows you to detect and recognize faces in images based on previously registered faces.

---

## 🚀 Technologies Used

- Python 3.x
- OpenCV (cv2)
- os (Python standard module)

---

## 📥 Installation

1. Clone the repository:

git clone https://github.com/SW-Samuel/facial_recognition.git

cd facial_recognition

2. Install the dependencies::

pip install requeriments.txt

---

## 🖼️ How to Use

### 1️⃣ Capture Photos of Known People

Run the `takePhoto.py` script.  
It will open your webcam and ask for the person's name. The image will be automatically saved in the `/images/` folder.

python takePhoto.py


➡️ Repeat this step for each person you want to register.

---

### 2️⃣ Train the Model with the Captured Photos

After capturing all the photos, run the training script to create the recognition model:

python iaModel.py


---

### 3️⃣ Run Real-Time Facial Recognition

Now, with the model trained, run the real-time facial recognition via webcam:

python ReconhecimentoFacial.py

The system will detect faces in real-time and display the recognized person's name.

---

## 📌 Possible Future Improvements

- Real-time detection with multiple cameras
- Export recognition results to CSV or a database
- Add a graphical user interface (GUI)
- Improve exception handling and user feedback

---

## 🧑‍💻 Author

[SW Samuel](https://github.com/SW-Samuel)
