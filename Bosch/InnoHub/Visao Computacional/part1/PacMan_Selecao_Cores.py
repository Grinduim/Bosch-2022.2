import cv2


def RBG2BGR(color: list):
    new_color = [color[-1], color[1], color[0]]
    return new_color


cap = cv2.VideoCapture("Materiais_opencv/pacman.mp4")

lower_color = (0, 200, 200)
max_color = (80, 255, 255)
red_lower = tuple(RBG2BGR([80, 0, 0]))
red_high = tuple(RBG2BGR([255, 50, 50]))
print(red_high)


while True:
    ret, img = cap.read()

    if not ret:
        break

    mask = cv2.inRange(img, lower_color, max_color)
    mask2 = cv2.inRange(img, red_lower, red_high)
    mask = mask | mask2
    # dilate = cv2.dilate(mask,kernel,iterations=4)

    c, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # c2, h2 = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    copia = img.copy()

    for cnts in c:
        (x, y, w, h) = cv2.boundingRect(cnts)
        cv2.rectangle(copia, (x, y), (x+w, y+h), (0, 255, 0), 2, cv2.LINE_AA)

    # for cnts in c2:
    #     (x, y, w, h) = cv2.boundingRect(cnts)
    #     cv2.rectangle(copia, (x, y), (x+w, y+h), (0, 255, 0), 2, cv2.LINE_AA)

    segm = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original", img)
    cv2.imshow("Contorno", copia)
    cv2.imshow("Objeto", segm)
    cv2.imshow("Mascara",mask)
    if cv2.waitKey(15) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
