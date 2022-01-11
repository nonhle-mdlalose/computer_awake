import pyautogui
import time

#setting FAILSAFE to False is enabled so that you can stop the execution of the program by manually moving the mouse to upper
#left corner of the screen
pyautogui.FAILSAFE = False

#use a while loop so that the script runs infinitely
while True:
    #sets the screen to sleep for 15 seconds so that it is not to frequent
    time.sleep(15)

    #loop to move the mouse
    for i in range(0, 100):
        pyautogui.moveTo(0, i * 5)

    #loop to press shift
    for i in range(0, 3):
        pyautogui.press('shift')



