import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}. png'.format(name)
    time.sleep(2)
    img = pyautogui.screenshot('test.png')
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

Button =tk.Button(
    frame,
    text="Take screenshot",
    command=screenshot)

Button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="QUIT",
command=quit)
close.pack(side=tk.LEFT)

root.mainloop()



screenshot()
