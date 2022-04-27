import cv2
import keyboard
import numpy as np
import matplotlib.pyplot as plt
import PIL
import tkinter as tk
from tkinter import *
from tkinter import ttk

global op
op = 0
image1 = cv2.imread("img1.jpg")
image2 = cv2.imread("img2.jpg")

img1 = cv2.resize(image1, dsize=(550, 350), interpolation=cv2.INTER_CUBIC)
img2 = cv2.resize(image2, dsize=(550, 350), interpolation=cv2.INTER_CUBIC)


suma = cv2.add(img1, img2)
resta = cv2.subtract(img1, img2)
division = cv2.divide(img1, img2)
multi = cv2.multiply(img1, img2)
#raiz = cv2.sqrt(img1)
potencia = cv2.pow(img1, 2)
potencia2 = cv2.pow(img2, 4)
conjuncion = cv2.bitwise_and(img1, img2)
disyuncion = cv2.bitwise_or(img1, img2)
negacion = cv2.bitwise_not(img1, img2)
##integral = cv2.threshold(img1, sum, -0)

##c = 255 / np.log(1 + np.max(image1))
##c = int(c)
##log_image = c * (np.log(image1 + 1))
##log_image = np.array(log_image, dtype = np.uint8)

##conca_verti = cv2.hconcat([img1, img2])
##conca_hori = cv2.hconcat([suma, resta])
#conca = cv2.vconcat([conca_verti, conca_hori])


while True:
    if keyboard.is_pressed("Y") or keyboard.is_pressed("y"):
        #cv2.imshow("Operaciones", conca)
        cv2.imshow("image1",img1), cv2.moveWindow("image1", 0, 0)
        cv2.imshow("image2",img2), cv2.moveWindow("image2", 975 , 0)
        cv2.imshow("Suma",suma), cv2.moveWindow("Suma", 500, 250)
        cv2.imshow("Resta", resta), cv2.moveWindow("Resta", 500, 280)
        cv2.imshow("Division", division), cv2.moveWindow("Division", 500, 310)
        cv2.imshow("Multiplicacion", multi), cv2.moveWindow("Multiplicacion", 500, 340)
        ##cv2.imshow("Raiz", raiz), cv2.moveWindow("Raiz", 400, 430)
        cv2.imshow("Potencia 2", potencia), cv2.moveWindow("Potencia 2", 500, 370)
        cv2.imshow("Potencia 4", potencia2), cv2.moveWindow("Potencia 4", 500, 400)
        cv2.imshow("Conjuncion", conjuncion), cv2.moveWindow("Conjuncion", 500, 430)
        cv2.imshow("Disyuncion", disyuncion), cv2.moveWindow("Disyuncion", 500, 460)
        cv2.imshow("Negacion", negacion), cv2.moveWindow("Negacion", 500, 490)
        ##cv2.imshow("Integral", integral), cv2.moveWindow("Integral", 400, 510)
        break


    
cv2.waitKey(0)
cv2.destroyAllWindows()
