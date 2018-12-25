import win32api, win32con
import os, sys, getopt, time
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

sleeptime = 0.7

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
    time.sleep(0.1)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN,fromx,fromy,0,0)
    time.sleep(0.2)
    move(tox,toy)
    time.sleep(0.2)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTUP,tox,toy,0,0)

loop = 1
dragline = 0
itemx = 0
itemy = 0
try:
    opts, args = getopt.getopt(sys.argv[1:], "hl:d:x:y:", ["loop=", "dragline=", "itemx=", "itemy="])
except getopt.GetoptError:
    print(os.path.basename(__file__) + ' -l <loop> -d <dragline> -x <itemx> -y <itemy>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print(os.path.basename(__file__) + ' -l <loop> -d <dragline> -x <itemx> -y <itemy>')
        sys.exit()
    elif opt in ("-l", "--loop"):
        loop = int(arg)
        print("loop %d" % loop)
    elif opt in ("-d", "--dragline"):
        dragline = int(arg)
        print("dragline %d" % dragline)
    elif opt in ("-x", "--itemx"):
        itemx = int(arg)
        print("itemx %d" % itemx)
    elif opt in ("-y", "--itemy"):
        itemy = int(arg)
        print("itemy %d" % itemy)
print("dragdown %d lines, sell item (%d, %d), loop for %d times" % (dragline, itemx, itemy, loop))

basex = 2300
incx = 170
basey = -320
incy = 185
i = loop
while i > 0:
    for j in range(0, dragline // 2):
        drag(basex - incx, basey + incy * 2, basex - incx, basey) # up 2 item line
        j = j + 1
    if(dragline % 2 == 1):
        drag(basex - incx, basey + incy, basex - incx, basey) # up 1 item line
    click(basex + incx * itemx, basey + incy * itemy)
    time.sleep(sleeptime+0.2)
    click(2700, -115)
    time.sleep(sleeptime)
    click(2460, -125)
    time.sleep(sleeptime)
    i = i - 1
    print("\r%-3d" % i, end = '', flush = True)
    if(i == 0):
        speak.Speak("Done")

# import pyautogui
# pyautogui.moveTo(100, 150)
# pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
# pyautogui.dragTo(100, 150)
# pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down
# pyautogui.click(100, 100)

# get global mouse position
# import win32gui
# import datetime
# start = datetime.datetime.now()
# end = datetime.datetime.now()
# elapsed = end - start
# while elapsed.seconds < 60: 
#     flags, hcursor, (x,y) = win32gui.GetCursorInfo()
#     end = datetime.datetime.now()
#     elapsed = end - start
#     print("\rx:%d, y:%d, %d" % (x, y, elapsed.seconds), end = "        \r")
