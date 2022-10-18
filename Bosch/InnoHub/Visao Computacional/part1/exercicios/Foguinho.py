import random

import numpy as np
import cv2
import color_palette

colors = np.array(color_palette.colors)
screen = np.zeros((500, 400), np.uint8)
DECAY = 3

while True:
    decay_values = np.random.randint(DECAY, size=(screen.shape[0]-1, screen.shape[1]))
    screen[:-1] = screen[1:] - decay_values
    screen[-1, :] = [0]
    screen[screen < 0] = 0

    tela = screen.copy()
    for i in range(37):
        tela[tela == i] = colors[i]
    cv2.imshow("Teste", tela)

    key = cv2.waitKey(50)
    if key == ord("q"):
        break



cv2.destroyAllWindows()