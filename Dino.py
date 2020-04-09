##--------------------------------------------------------------
import ctypes
import time
from ctypes import windll, Structure, c_long, byref
from PIL import ImageGrab
from pynput.keyboard import Key, Controller
import os
from PIL import Image
##--------------------------------------------------------------

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
    
def Get():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return([pt.x,pt.y])

def Screen():
        snapshot = ImageGrab.grab(bbox=(620,310,680,311))
        save_path = "C:/Users/theot/Desktop/Dino Python/shot.jpg"
        snapshot.save(save_path)

def TestPix(x,y,img):
    r,g,b = img.getpixel((x,y))
    if (r < 100):
        return 1
    return 0

def TestPixMult(x,y,n,img):
    N = 0
    r = 0
    g = 0
    b = 0
    for x in range(n):
        N += TestPix(x,y,img)
    return N

def jouer():
    
    keyboard = Controller()

    VitesseDecalage = 0.025
    AttenteBlanc = 0.001
    AttenteNoir = 0.08
    
    x1 = 700
    y1 = 305
    
    x2 = 750
    y2 = 307

    T = 0
    t = 0
    
    while(Get()[0]<1000):                             #Check souris

        T += VitesseDecalage
        t = int(T)                                    #Recupere temps


        x1 = x1 + t 
        x2 = x2 + t                                   #Decalage Screen
        L = x2 - x1                                   #Taille image 
        H = y2 - y1
        x = 0                                         #Coordonées pixel etudier
        y = 1                                         #Image de 1 pixel de haut
        Blanc = 0                                     # Nombre de blanc avant l'obstacle
        Noir = 0                                      # Nombre de noir (taille de l'obstacle)
        img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        
        while (x != L  and TestPix(x,y,img) == 0):    #On compte le nombre de case blanche
            x += 1
            Blanc += 1
        
        while (x <= L-10  and TestPixMult(x,y,20,img) > 1):  #On compte le nombre dde case noir , on check plusieur obtable voir si y en a deriere
            x += 1
            Noir += 1

        if(Noir > 0):                                        #Si y a un obstacle on attend plus ou moins lomgtemps si y a des blanc avant
            time.sleep(Blanc*AttenteBlanc)
            keyboard.press(Key.space)
            
            time.sleep(Noir*AttenteNoir)                            #Si y a des noir on saute plus lomgtemps
            keyboard.release(Key.space)

            keyboard.press(Key.down)                       
            time.sleep(0.05)                            #Si y a des noir on saute plus lomgtemps
            keyboard.release(Key.down)

time.sleep(2)
jouer()





