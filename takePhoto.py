import cv2
import os

nome = input("Digite o nome da pessoa: ").strip()

caminho = f"imagens/{nome}"
os.makedirs(caminho, exist_ok=True)

webcam = cv2.VideoCapture(0)
contador = 0

while True:
    _, frame = webcam.read()
    cv2.imshow("Captura - Pressione ESC para sair", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

    if contador % 10 == 0:
        cv2.imwrite(f"{caminho}/{contador}.jpg", frame)

    contador += 1

webcam.release()
cv2.destroyAllWindows()
