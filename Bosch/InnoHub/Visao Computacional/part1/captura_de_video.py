import cv2
import numpy as np

cap = cv2.VideoCapture("Materiais_opencv/pacman.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", frame)

    if not ret:
        break

    if cv2.waitKey(1) == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
