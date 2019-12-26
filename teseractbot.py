from PIL import ImageGrab, ImageOps
import time
import pyautogui
from numpy import *      
       
class Cordinates():
    replayBtn = (340,390)
    dianosaur = (171,395)
    #240= x cordinates to check for the tress 
    #y cordinates =420
def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jumping through code.....!!!   ")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dianosaur[0]+280,Cordinates.dianosaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(graysImage.getcolors())
    print(a.sum())


restartGame()
time.sleep(1)

while True:
    pressSpace()

imageGrab()

