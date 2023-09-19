import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def iscollide(data):
    # draw rectangle for cactus
    for i in range(724, 75):
        for j in range(240, 295):
            if data[i, j] >100 and data[i,j]<200:
                hit("up")
                return 
                
    # Draw rectangle for birds
    for i in range(694, 775):
        for j in range(160, 255):
            if data[i, j] >100 and data[i,j]<200:
                hit("up")
                return 
    return 


if __name__ == "__main__":
    print("Dino Game will start in 2 seconds...")

    time.sleep(2)
    hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)
        #     # draw rectangle for cactus
        #     for i in range(694, 775):
        #         for j in range(260, 285):
        #             data[i, j] = 0
                    

        # # Draw rectangle for birds
        #     for i in range(694, 775):
        #         for j in range(160, 255):
        #             data[i, j] = 171
                    
        #     image.show()
        #     break