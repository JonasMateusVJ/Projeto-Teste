# quais são os passos manuais que devo transformar em código
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1165,435, duration=1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1070,574, (0, 0, 0)):
        click(1070,574)
    if pyautogui.pixelMatchesColor(1127,570, (0, 0, 0)):
        click(1127,570)
    if pyautogui.pixelMatchesColor(1198,573, (0, 0, 0)):
        click(1198,573)
    if pyautogui.pixelMatchesColor(1265,570, (0, 0, 0)):
        click(1265,570)
#https://gameforge.com/pt-BR/littlegames/magic-piano-tiles/#