from ctypes import pointer
from turtle import width
import cv2
import numpy as np

# if house is equal a 0 == null 
# if equal a 1 == X
# if equal a 2 == O

height = 1000
width = 900

def create_hash(img):
    global height,width
    #make line in horizontal
    cv2.line(img,(0,400),(900,400),(255,255,255),5)
    cv2.line(img,(0,700),(900,700),(255,255,255),5)

    #make line in vertical
    cv2.line(img,(300,100),(300,1100),(255,255,255),5)
    cv2.line(img,(600,100),(600,1100),(255,255,255),5)

def fill_hash(img,game):
    for i in game:
        for j in game[i]:
            if j == 0:
                continue
            elif j == 1:
                pass
                #draw X
            elif j == 2:
                pass
                #draw O


def draw_circle(img, posx,posy):
    cv2.circle(img,(posx,posy),20,(255,255,255),3)

def draw_x(img,squarex,squarey):
    if squarex > 0:
        posx = 300* squarex + 20
    else:
        posx = 20

    if squarey > 0:
        posy = 100 + (300*squarey + 20)
    else:
        posy = 120

    cv2.line(img,(posx,posy),(posx+220,posy+220),(255,255,255),3)
    cv2.line(img,(posx,posy+200),(posx+220,posy),(255,255,255),3)

game =  np.zeros((3,3),np.uint64)
print(game)
screen = np.zeros((height,width,3),np.uint8)
create_hash(screen)
draw_x(screen,1,1)
cv2.imshow("jogo",screen)
cv2.waitKey(0) 
cv2.destroyAllWindows()