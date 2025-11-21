from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import time
import pydirectinput
import threading
from threading import Thread
import numpy as np



prev = [0,0]
coordinates=[[585, 275],[835, 275],[1085, 275], [1335, 275],
             [585, 465],[835, 465],[1085, 465],[1335, 465],
             [585, 675],[835, 675],[1085, 675], [1335, 675]]#,
             #[585, 875],[835, 875],[1085, 875], [1335, 875]]
kolejka=[]
counter=0
    

#start - zarzucić na wszystkich 1+2
def rzut12():
    r0=random.randint(2,6)
    x_arr = [275, 465 ,675]#875]
    y_arr = [585,835,1085,1335]
    for x in x_arr:
        for y in y_arr:
            r2=random.randint(-25,25)
            r3=random.randint(-25,25)
            r4=random.randint(-25,25)
            r5=random.uniform(0.10,0.15)
            r6=random.uniform(0.05,0.10)
            win32api.SetCursorPos((y+r2,x+r3))
            time.sleep(r5)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
            pydirectinput.press('1')
            time.sleep(r6)
            pydirectinput.press('2')


        

def polow(a,b): #+rzut
    c=coordinates[int(a)]
    r1=random.randint(-50,50)
    r2=random.randint(20,60)
    r3=random.uniform(0.25,0.35)
    x=c[0]+r1
    y=c[1]+r2
    #wycentrowanie okna     
    #pyautogui.moveTo(x, y,r3)
    time.sleep(0.01)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    #print('okno polow wycentrowane',a,b)
    time.sleep(0.01)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    #wcisnąć x razy spacje w odstępach rand w tym obszarze + rand
    if (random.randint(0,20)<=15):
        #print('wyłowiono')
        for i in range(b):
            #win32api.SetCursorPos((x,y))
            #pydirectinput.press('space')
            #print('spacja')
            time.sleep(random.uniform(0.06,0.12))
    r10=random.uniform(0,1)
    r11=random.randint(-25,25)
    r12=random.randint(-25,25)
    r13=random.uniform(0.1,0.15)
    r14=random.uniform(0.05,0.10)
    czasrzutu=r10+7
    n=c[0]+r11
    m=c[1]+r12
    time.sleep(czasrzutu)
    #win32api.SetCursorPos((n,m))
    time.sleep(r13)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.01)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    #pydirectinput.press('1')
    time.sleep(r14)
    #pydirectinput.press('2')
    #print('zarzucono i wyczyszczono')
    kolejka.remove([a,b])
    global counter
    counter=counter+1
    #print(counter)
    print("")

            
#rzut12() 
def main():
    while keyboard.is_pressed('x') == False: #+wykrywacz gma
        image_list = ['2.png','3.png','4.png','5.png']
        for image in image_list:
            y=pyautogui.locateCenterOnScreen(image,region=(460,125,1000,620), grayscale=True, confidence=0.60)
            if y !=None:
                x=int(image[0])
                z=[x,y[0],y[1]]
                #global prev
                for coord in coordinates:
                    if (coord[0]-50 <= y[0] <= coord[0]+50)and (coord[1]-100 <= y[1] <= coord[1]+100):
                        nrokna=coordinates.index(coord)
                        #print([nrokna,x])
                        retrieved_elements = list(filter(lambda c: nrokna == c[0], kolejka))
                        if len(retrieved_elements)==0: #and prev!=[nrokna,x]:
                            kolejka.append([nrokna,x])
                            print([nrokna,x])
                            thread1 = threading.Thread(target=polow, 
                                                   args=(nrokna, x))
                            thread1.start()
                            #prev=[nrokna,x]
                            #print(kolejka)
                            #thread polow
                            #break

core=Thread(target=main)
core.start()





    


