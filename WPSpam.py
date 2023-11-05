import pyautogui as pag
import time as t

t.sleep(4)  # Delay for your clicking
# Click the where you want to send or write
for i in range(50):
    pag.typewrite("Hello")
    pag.press('enter')
