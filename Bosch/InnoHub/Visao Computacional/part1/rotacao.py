import cv2


def main():
    yodinha = cv2.imread('./Materiais_opencv/yodinha.jpg')

    (h,w) = yodinha.shape[:2]
    center = (w//2, h//2)
    m = cv2.getRotationMatrix2D(center, 90, 1.0)
    imgrot = cv2.warpAffine(yodinha, m, (w, h))


    cv2.imshow("janela", yodinha)
    cv2.imshow("rotadcionada", imgrot)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    # Y X
    flip_horizontal = yodinha[::-1, :]
    flip_vertical = yodinha[:, ::-1]
    flip_todos = yodinha[::-1,::-1]

    cv2.imshow("flip horizontal ", flip_horizontal)
    cv2.imshow("flip vertical ", flip_vertical)
    cv2.imshow("flip todos ", flip_todos)
    cv2.imshow("janela", yodinha)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

if __name__ == "__main__":
    main()