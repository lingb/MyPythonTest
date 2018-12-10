import win32api, win32con
import time

def move(x,y):
    win32api.SetCursorPos((x,y))

def click(x,y):
    move(x,y)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def drag(fromx, fromy, tox, toy):
    move(fromx,fromy)
    time.sleep(0.4)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN,fromx,fromy,0,0)
    time.sleep(0.4)
    move(tox,toy)
    time.sleep(0.4)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTUP,tox,toy,0,0)



sleeptime = 0.4
x = 0
while x < 2:
    # drag(2200, 250, 2200, 60) # up 1 item line
    # click(2800, 250) # item 4, 4
    # click(2640, 250) # item 3, 4
    # click(2480, 250) # item 2, 4
    # click(2320, 250) # item 1, 4
    # drag(2200, 250, 2200, -160) # up 2 item line
    # click(2800, 60) # item 4, 3
    # click(2640, 60) # item 3, 3
    # click(2480, 60) # item 2, 3
    # click(2320, 60) # item 1, 3
    drag(2200, 250, 2200, -300) # up 3 item line
    click(2320, 60) # item 1, 3
    time.sleep(sleeptime)
    click(2800, 0)
    time.sleep(sleeptime)
    click(2400, 0)
    time.sleep(sleeptime+0.4)
    x = x + 1

# move(2480,250) # item 2, 4

# import pyautogui
# pyautogui.moveTo(100, 150)
# pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
# pyautogui.dragTo(100, 150)
# pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down
# pyautogui.click(100, 100)

