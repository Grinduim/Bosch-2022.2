import cv2
import numpy as np

video = cv2.VideoCapture("Materiais_opencv/traffic_light.mp4")

green_lower = (70, 0, 255)
green_upper = (101, 255, 255)

yellow_lower = (20, 0, 255)
yellow_upper = (40, 255, 255)

red_lower = (0, 0, 255)
red_upper = (10, 255, 255)

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_g = cv2.inRange(frame_hsv, green_lower, green_upper)
    mask_y = cv2.inRange(frame_hsv, yellow_lower, yellow_upper)
    mask_r = cv2.inRange(frame_hsv, red_lower, red_upper)

    current_state = "| "
    if mask_g.sum() > 100000:
        current_state += "green |"
    if mask_y.sum() > 100000:
        print(mask_y.sum(), mask_r.sum())
        current_state += "yellow |"
    if mask_r.sum() > 100000:
        current_state += "red |"

    cv2.putText(frame, current_state, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

    cv2.imshow("Padrao", cv2.resize(frame, None, fx=0.5, fy=0.5))
    cv2.imshow("g", cv2.resize(mask_g, None, fx=0.5, fy=0.5))
    cv2.imshow("mask_y", cv2.resize(mask_y, None, fx=0.5, fy=0.5))
    cv2.imshow("mask_r", cv2.resize(mask_r, None, fx=0.5, fy=0.5))

    if cv2.waitKey(5) == ord('q'):
        break
