import cv2
import numpy as np

image = cv2.imread("../Materiais_opencv/arroz.bmp")
image = cv2.GaussianBlur(image, (13, 13), 0)

lower = (160, 215, 215)
upper = (255, 255, 255)

mask = cv2.inRange(image, lower, upper)

c, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

copia = mask.copy()
count = 0
for cnts in c:
    (x, y, w, h) = cv2.boundingRect(cnts)
    cv2.putText(image, f"{count+1}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 255), thickness= 2)
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2, cv2.LINE_AA)
    count +=1


cv2.putText(image, f"Total de Arroz: {count}", (15, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), thickness=2)


cv2.imshow("original", cv2.resize(image, None, fx=0.6, fy=0.6))
cv2.imshow("Mascara", cv2.resize(mask, None, fx=0.6, fy=0.6))


cv2.waitKey(0)
cv2.destroyAllWindows()
