# Text Spammer bot by RKM
import pyautogui as pag
import time as t

x = int(input("Enter time delay: "))
y = int(input("Enter test limit: "))
z = input("Enter the text: ")

print(f"Click anywhere in {x} Seconds...")

t.sleep(x)

for i in range(y):
    pag.typewrite('z')
    pag.press('enter')
print("Operation Successfull!!")
