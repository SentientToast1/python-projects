from pyautogui import *
import pyautogui as pg
import time
import keyboard
import random
import win32api, win32con

# x1= 490 x2=560 x3=630 x4=700

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pg.pixel(490, 500)[0] == 0:
        click(490,500)
    if pg.pixel(560, 500)[0] == 0:
        click(560, 500)
    if pg.pixel(630, 500)[0] == 0:
        click(630, 500)
    if pg.pixel(700, 500)[0] == 0:
        click(700, 500)