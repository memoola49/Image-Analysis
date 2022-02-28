import os
import cv2
import numpy as np
from cv2 import imread

Puntos= np.zeros((2,2),np.int64)

contador=0

def cambiarpixel(x, y):
    R = input("Ingrese valor para R= ")
    print("\n")
    G = input("Ingrese valor para G= ")
    print("\n")
    B = input("Ingrese valor para B= ")
    print("\n")
    print("x , y, R , G , B")
    print(x," ",y," ",R," ",G," ",B)
    img[y,x]=(R,G,B)
    cv2.imshow("PixelCambiado",img)



def clicks(event,x,y,flags,params):
    global contador
    if event == cv2.EVENT_LBUTTONDOWN:
        valorx = x
        valory = y
        cambiarpixel(valorx, valory)
    if event == cv2.EVENT_RBUTTONDOWN:
        Puntos[contador]=x,y
        contador = contador + 1

img=imread("ejemplo1.bmp",1)


while True:
    if contador == 2:
        x1 = Puntos[0][0]
        y1 = Puntos[0][1]
        x2 = Puntos[1][0]
        y2 = Puntos[1][1]
     #   cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)

        img_marco = img[y1:y2,x1:x2]
        cv2.imshow("Cortada",img_marco)
        contador=0
    cv2.imshow("Original",img)
    cv2.setMouseCallback("Original",clicks)

    cv2.waitKey(1)


