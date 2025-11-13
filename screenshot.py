import time
import pyautogui

def screenshot():
    time.sleep(2)
    img = pyautogui.screenshot('test.png')
    img.show()


screenshot()
# I changed this code with the below because in upper case code
# The file name is always show the test 
#due to that i am going to fix the changes with through 
import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}. png'.format(name)
    time.sleep(2)
    img = pyautogui.screenshot('test.png')
    img.show()

screenshot()
