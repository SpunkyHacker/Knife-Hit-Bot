from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import linecache

KNIFE = (270,190)
RESET = (278,734) #if Red  == 0 then its reset button
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
# def deleteData(line):
#     print(line)
#     with open("database.txt","r") as file:
#         data = file.readlines()
#     data[line-1] = "\n"
#     with open('database.txt','w') as file:
#         file.writelines(data)
#     print('deleted data')

def deleteData():
    with open("database.txt") as file:
        data = file.readlines()
    data[-1] = ""
    with open('database.txt','w') as file:
        file.writelines(data)


def main():
    start()
    sleep(1)
    line = 1
    while keyboard.is_pressed('q') == False:
        flag = checkDatabase(line)
        if flag == True:
            time = getTimeInDatabase(line)
            sleep(time)
            click(KNIFE)
            x,y=RESET
            sleep(0.5)
            if pyautogui.pixel(x,y)[0] == 0:
                print("Data in database is wrong!")
        elif flag == False:
            time = getRandomTime()
            sleep(time)
            click(KNIFE)
            x,y=RESET
            sleep(0.5)
            if pyautogui.pixel(x,y)[0] != 0:
                appendDatabase( time)
            else:
                print('came in here')
                break
                click(RESET)
        line+=1
        




                    


if __name__ == "__main__":
    main()
