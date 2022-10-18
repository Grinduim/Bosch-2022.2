import cv2
import numpy as np

img = cv2.imread('Materiais_opencv\\valve.png')

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


edges_y = cv2.Sobel(img_gray, -1, 0, 1, ksize=5)
edges_x = cv2.Sobel(img_gray, -1, 1, 0, ksize=5)
edges = cv2.Sobel(img_gray, -1, 1, 1, ksize=5)

cv2.imshow("1",edges)
cv2.imshow("2",edges_y)
cv2.imshow('3',edges_x)

cv2.waitKey(0)
cv2.destroyAllWindows()