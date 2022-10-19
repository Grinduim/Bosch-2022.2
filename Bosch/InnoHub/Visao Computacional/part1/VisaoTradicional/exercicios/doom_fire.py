import color_palette
import numpy as np
import cv2

FIRE_DECAY = 4
def update_fire(matrix):
            
    decay_values = np.random.randint(FIRE_DECAY, size=(matrix.shape[0]-1, matrix.shape[1]))
    matrix[:-1] = matrix[1:] - decay_values
    matrix[matrix < 0] = 0
        
    return matrix

if __name__=="__main__":

    fire_matrix = np.zeros((100, 100))
    fire_matrix[-1] = 36
    # fire_matrix[-1] = np.random.randint(20, 36, 100)

    image_fire = np.zeros((fire_matrix.shape[0], fire_matrix.shape[1], 3), dtype=np.uint8)
    color_palette.colors = np.asarray(color_palette.colors)[:,::-1]
    
    while True:
    
        fire_matrix = update_fire(fire_matrix)
        # fire_matrix[-1] = np.random.randint(0, 36, 100)

        for i in range(37):
            image_fire[fire_matrix == i] = color_palette.colors[i]

        cv2.imshow("doom fire", cv2.resize(image_fire, None, fx=6, fy=6))
        density = fire_matrix.copy()
        density /= 36
        density *= 255
        density = density.astype(np.uint8)
        cv2.imshow("matrix normalized", cv2.resize(density, None, fx=6, fy=6))
        cv2.imshow("matrix", cv2.resize(fire_matrix.astype(np.uint8), None, fx=6, fy=6))
        key = cv2.waitKey(50)
        if key == ord("f"):
            fire_matrix[-1] = 0
        elif key == ord("g"):
            fire_matrix[-1] = 36