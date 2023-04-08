from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import linecache



# X:  283 Y:  733 RGB: (  0, 216,  54)  r == 4 then its game 

# play button x 480 y 731 0,178,71

def start():
    click(480,731)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def getRandomTime():
    time =  random.randint(1,5)
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

def appendDatabase(linenum , time):
    with open("database.txt") as file:
        data = file.readlines()
    try:
        data[linenum - 1] = str(time) + "\n"
        with open("database.txt", 'w') as file:
            file.writelines(data)
    except IndexError:
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
    countdown = 1
    while keyboard.is_pressed('q') == False: # making sure we can exit
        start() # for clicking the start button in the start of the game
        while True: # comes here after geting reset button
            countdown = 1 
            while True: #illitrate until successful 
                print(countdown)
                if pyautogui.pixel(283, 733)[0] == 0: #checks for reset button
                    print("countdown before deleting",countdown)
                    click(283, 733) #clicks reset
                    deleteData()
                    break
                flag = checkDatabase(countdown) #checks for pre loaded data
                if flag: # gets the pre loaded data and clicks
                    recordedTime = getTimeInDatabase(countdown)
                    sleep(recordedTime)
                    click(283, 733)
                    if pixel(283, 733)[0] == 4: # check if we are in game  " that is the previous move was successful"
                        countdown+=1
                    else:
                        print('try failed')
                else: # generates randomly and clicks
                    newTime = getRandomTime()
                    sleep(newTime)
                    click(283, 733)
                    if pixel(283, 733)[0] == 4: # check if we are in game  " that is the previous move was successful"
                        appendDatabase(countdown,newTime) #stores the new data
                        countdown+=1
                    else:
                        print('try failed')
                    


if __name__ == "__main__":
    main()
