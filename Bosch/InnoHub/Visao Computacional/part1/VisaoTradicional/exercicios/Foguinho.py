import random

import numpy as np
import cv2
import color_palette

colors = np.asarray(color_palette.colors)
fire_matrix = np.zeros((500, 400), np.uint8)
DECAY = 2
fire_image = np.zeros((fire_matrix.shape[0], fire_matrix.shape[1], 3), dtype=np.uint8)

while True:
    decay_values = np.random.randint(DECAY, size=(fire_matrix.shape[0] - 1, fire_matrix.shape[1]))
    fire_matrix[:-1] = fire_matrix[1:] - decay_values
    fire_matrix[-1] = 36
    fire_matrix[fire_matrix < 0] = 0

    # print(colors[abs(screen[200, 300] - 219)])

    # tela = np.array((500, 400, 4))
    # for i in range(screen.shape[0]):
    #     for y in range(screen.shape[1]):
    #         tela[i, y] =

    for i in range(37):
        fire_image[fire_matrix == i] = color_palette.colors[i]
    cv2.imshow("Teste", fire_image)

    key = cv2.waitKey(50)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
