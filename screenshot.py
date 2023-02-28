import win32gui
import win32ui
import win32con
import cv2
import numpy as np
import timeit
import ctypes
import os
from PIL import ImageOps
from time import sleep
from ctypes import wintypes
w = 1920 # set this
h = 1080 # set this
bmpfilenamename = "out.bmp" #set this

hwnd = win32gui.FindWindow(None, "Gaules - Twitch - Google Chrome")
# hwnd = win32gui.FindWindow(None, "Tibia")

# user32 = ctypes.windll.user32
# gdi32 = ctypes.windll.gdi32

def screenshot():
    wDC = win32gui.GetWindowDC(hwnd)
    # wDC = user32.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0), (w, h), dcObj, (0,0), win32con.SRCCOPY)
    bmpinfo = dataBitMap.GetInfo()
    bmpstr = dataBitMap.GetBitmapBits(True)
    # img = np.ndarray(shape=(h, w, 4), dtype=np.uint8, buffer=bmpstr)
    img = np.frombuffer(bmpstr, dtype=np.uint8)
    img.shape = (bmpinfo['bmHeight'], bmpinfo['bmWidth'], 4)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    return gray_img

sct = screenshot()
cv2.imwrite('screenshot.png', sct)
res = timeit.repeat(lambda: screenshot(), repeat=10, number=1)
print('res', res)

# while True:
#     sleep(0.03333333333)
#     screenshot()