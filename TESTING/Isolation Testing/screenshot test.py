import socket
import sys
import os
import time

import cv2
from mss import mss
screenshot_counter = 1
def takeScreenshot(screenshot_counter):
    sct = mss()
    sct.shot(output='./logs/screen{}.png'.format(screenshot_counter))  # taking screenshot

    picsize = os.path.getsize('./logs/screen{}.png'.format(screenshot_counter))
    size = str(picsize)
    #self.client.send(size.encode("utf-8"))  # sending size
    time.sleep(0.1)

    screen = open('./logs/screen{}.png'.format(screenshot_counter), 'rb')
    tosend = screen.read()
    #self.client.send(tosend)  # sending actual file

    screen.close()
    #os.remove('./logs/screen{}.png'.format(screenshot_counter))  # removing file from host
    screenshot_counter += 1
    # saving the file


 #   with open(f'../receivedfile/{time.time()}.png', 'wb+') as screen:
  #      screen.write(fullscreen)

    print("*** File saved ***")


input()
# takeScreenshot(screenshot_counter)
input()
def single():
    ## SINGLE SCREENSHOT
    sct = mss()
    sct.shot(output='./logs/screenshot_test.png')  # taking screenshot
    print("Screenshot taken")
    input()

## SCREENSHOT WITH NUMBER IN FILENAME
def number():

    sct = mss()
    sct.shot(output='./logs/screenshot{}.png'.format(screenshot_counter))  # taking screenshot
    print("Screenshot {} taken".format(screenshot_counter))
    input()
## 10 ITERATIVE SCREENSHOTS AT 5 SECOND INTERVALS
    ## USES I FOR FILENAME
def iterative():

    sct = mss()
    screenshot_counter = 0
    for i in range(10):
        sct.shot(output='./logs/loop_screenshot{}.png'.format(i))  # taking screenshot
        print("Screenshot {} taken".format(i))
        time.sleep(0.5)
    input()
## USES COUNTER FOR FILENAMES
def counter():
    sct = mss()
    screenshot_counter = 0
    for i in range(100):
        sct.shot(output='./TESTING/logs/Video/loop_screenshot{}.png'.format(screenshot_counter))  # taking screenshot
        #print("Screenshot {} taken".format(screenshot_counter))
        screenshot_counter += 1
        time.sleep(int(1/24))
input()
def allscreens():
    sct = mss()
    multi = "_multi"
    sct.shot(mon=-1, output='./logs/screen{}.png'.format(multi))

#allscreens()
input("start")
counter()
input("Done")

def test2():
    path = './TESTING/logs/Video'
    cv2.namedWindow("sstest")
    with os.scandir('./TESTING/logs/Video') as entries:
        for entry in entries:
            print(entry.name)
            p = str(path) + str("/")+str(entry.name)
            x = cv2.imread(p)
            cv2.imshow("sstest", x)
            cv2.waitKey(0)
test2()