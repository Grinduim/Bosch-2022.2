import cv2
import numpy as np

cap = cv2.VideoCapture("./Materiais_opencv/traffic_light.mp4")

# Definindo ranges para detectar amarelo
lower_range_g = (70, 0, 255)
upper_range_g = (90,255, 255)

lower_range_y = (20, 0, 255)
upper_range_y = (40,255, 255)

lower_range_r = (0, 0, 255)
upper_range_r = (10, 255, 255)

kernel = np.ones((3, 3))
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Aplicando inRange para obter mascara
    mask_g = cv2.inRange(frame_hsv, lower_range_g, upper_range_g)
    mask_y = cv2.inRange(frame_hsv, lower_range_y, upper_range_y)
    mask_r = cv2.inRange(frame_hsv, lower_range_r, upper_range_r)
    # mask_g = cv2.dilate(mask_g,kernel, iterations=10)
    # mask_y = cv2.dilate(mask_y,kernel, iterations=10)
    # mask_r = cv2.dilate(mask_r,kernel, iterations=10)

    current_state = "| "
    if mask_g.sum() > 100000:
        current_state += "green |"
    if mask_y.sum() > 100000:
        print(mask_y.sum(), mask_r.sum())
        current_state += "yellow |"
    if mask_r.sum() > 100000:
        current_state += "red |"

    cv2.putText(frame, current_state, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1)
    # Resultados
    cv2.imshow('Imagem original', cv2.resize(frame, None, fx=0.5, fy=0.5))
    cv2.imshow('g', cv2.resize(mask_g, None, fx=0.5, fy=0.5))
    cv2.imshow('y', cv2.resize(mask_y, None, fx=0.5, fy=0.5))
    cv2.imshow("r", cv2.resize(mask_r, None, fx=0.5, fy=0.5))

    key = cv2.waitKey(100)
    if key == ord("q"):
        break
cv2.destroyAllWindows()