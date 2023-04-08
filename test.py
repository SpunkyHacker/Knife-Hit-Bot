from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import linecache

KNIFE = (270,190)
RESET = (278,740) #if Red  == 0 then its reset button
START = (414,198)

def start():
    click(START)

def click(coords):
    print("clickedd")
    win32api.SetCursorPos(coords)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def getRandomTime():
    time =  random.randint(1,3)
    print('got random time')
    return time

def checkDatabase(linenum): #OK
    print('checked Database')
    line = linecache.getline(r"database.txt", linenum)
    if len(line) == 0:
        return False
    else:
        return True

def getTimeInDatabase(linenum): #OK
    print('getting time')
    line = linecache.getline(r"database.txt", linenum)
    try: 
        return int(line)
    except ValueError:
        return 0

def appendDatabase(time):
    with open("database.txt",'a') as file:
        file.write(str(time)+"\n")
    print('appended time')

def deleteData():
    with open("database.txt") as file:
        data = file.readlines()
    data[-1] = ""
    with open('database.txt','w') as file:
        file.writelines(data)

deleteData()