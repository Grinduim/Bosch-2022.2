import cv2
import numpy as np

img = cv2.imread("./Materiais_opencv/yodinha.jpg")

kernel1 = np.ones((3, 3), np.float32)/9
img_blur = cv2.filter2D(img,-1,kernel1)

kernel2 = np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])
img_sharpen = cv2.filter2D(img,-1,kernel2)

cv2.imshow("Yodinha original",img)
cv2.imshow("Yodinha com blur",img_blur)
cv2.imshow("Yodinha com sharpen",img_sharpen)

cv2.waitKey(0)
cv2.destroyAllWindows()