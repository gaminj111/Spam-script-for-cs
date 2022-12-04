import pyautogui
import time
a = 1
time.sleep(12.5)
while a < 10:
    with pyautogui.hold('l'):
        pyautogui.press(['enter', 'enter', 'enter', 'enter', 'enter', 'enter'])
    a = a + 1