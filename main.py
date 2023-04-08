from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import linecache

KNIFE = (270,190)
RESET = (278,734) #if Red  == 0 then its reset button
START = [(414,198),(400,740)]
reseted = False
count = 0

def start():
    click(START[1])

def click(coords):
    print("clicked..")
    win32api.SetCursorPos(coords)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def getRandomTime():
    time =  random.uniform(1.0,3.0)
    time = round(time,1)
    print("generated random number:",time)
    return time

def checkDatabase(linenum): #OK
    with open('database.txt') as file:
        data = file.readlines()
    try:
        if len(data[linenum-1]) > 0:
            return True
        else:
            return False    
    except IndexError:
        return False

def getTimeInDatabase(linenum): #OK
    global count
    count+=1
    line = linecache.getline(r"database.txt", linenum)
    print(f'{str(count)} --> gotfromDatabase: {line}')
    try: 
        return float(line)
    except ValueError:
        return 0

def appendDatabase(time):
    global count
    count+=1
    with open("database.txt",'a') as file:
        file.write(str(time)+"\n")
    print(f'{str(count)} --> appended: {time}')

def deleteData():
    with open("database.txt") as file:
        data = file.readlines()
    data[-1] = ""
    with open('database.txt','w') as file:
        file.writelines(data)


def main():
    start() 
    line = 1
    while keyboard.is_pressed('q') == False:
        flag = checkDatabase(line)
        print(flag,line)
        if flag == True:
            sleep(1)
            t = getTimeInDatabase(line)
            print("i wanted to wait:",t)
            time.sleep(t)
            
            click(KNIFE)
            x,y=RESET
            print("@")
            sleep(2)
            if pyautogui.pixel(x,y)[0] == 0:
                print("Data in database is wrong!")
                break
        elif flag == False:
            sleep(1)
            t = getRandomTime()
            sleep(t)
            click(KNIFE)
            x,y=RESET
            print("#")
            sleep(2)
            if pyautogui.pixel(x,y)[0] != 0:
                appendDatabase(t)

            else:
                click(RESET)
                print("#####\nRESETED\n#####")
                line = 0
        line+=1
        
        




                    


if __name__ == "__main__":
    main()
