#!/usr/bin/env python

import sys
import win32api, win32con
from ctypes import Structure, windll, c_uint, sizeof, byref

# Time
TIME_THRESH = 600

# Locations
X_LOC = 200
Y_LOC = 200

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]
 
def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def main():

    last_input = int(get_idle_duration())

    if last_input > TIME_THRESH:
        click(X_LOC, Y_LOC)

    return 0


#############################
if __name__ == "__main__":
    sys.exit(main())
#############################