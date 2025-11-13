import time
import pyautogui

def screenshot():
    time.sleep(2)
    img = pyautogui.screenshot('test.png')
    img.show()

screenshot()