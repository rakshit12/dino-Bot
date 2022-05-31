import pyautogui 
from PIL import Image, ImageGrab

import time
def iscollide(data):
    for i in range(270, 300):

        for j in range(260,340):

            if data[i,j] < 100:
                pyautogui.keyDown('down')
                return
    for i in range(320, 400):
        for j in range(380, 450):
            if data[i, j] < 100:
               pyautogui.keyDown('up')
               return
if __name__ == "__main__":

    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    while True:
        image = ImageGrab.grab() 
        data = image.load()
        iscollide(data)

    #for i in range(320, 400):

        #for j in range(380, 450):
            #data[i, j] = 0
    #for k in range(270, 300):
        #for z in range(260,340):
            #data[k,z]=171
    #image.show()
