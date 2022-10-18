import cv2
import numpy as np

img = cv2.imread("Materiais_opencv/yodinha.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(7,7),0)

retval, thresh = cv2.threshold(blur,100,255,cv2.THRESH_BINARY)
retivalI, threshI = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV)

resultado = np.vstack([np.hstack([img, blur]),
                       np.hstack([thresh, threshI])])

cv2.imshow("reusltado",resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
