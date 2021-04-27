import os
from zipfile import ZipFile

import cv2

def firstattempt():
    cv2.namedWindow("display frame")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("display frame", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(0)
        if key == 27:  # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("display frame")

def secondattempt():
    cv2.namedWindow("display frame")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("display frame", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("display frame")


def capture():
    counter = 0
    vc = cv2.VideoCapture(0)
    if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
        cv2.imwrite('./logs/Video/video{}.png'.format(counter), frame)
        counter += 1
    else:
        rval = False
    fr = 200
    while fr > 0: #rval:
        fr -= 1
        if len(str(counter)) < 4:
            spacer = "0" * (4-int((len(str(counter)))))
        cv2.imwrite('./logs/Video/video{}{}.png'.format(spacer, counter), frame)
        counter += 1
        rval, frame = vc.read()
        cv2.waitKey(int(1000/24))
    vc.release()


def play():

    cv2.namedWindow("Playback")
    path = './logs/Video'
    for item in os.listdir(path):
        x = cv2.imread(item)
        cv2.imshow("Playback", x)
    cv2.destroyWindow("Playback")

def test2():
    path = './logs/Video'
    cv2.namedWindow("P2")
    with os.scandir('./logs/Video') as entries:
        for entry in entries:
            print(entry.name)
            p = str(path) + str("/")+str(entry.name)
            x = cv2.imread(p)
            cv2.imshow("P2", x)
            cv2.waitKey(0)
    cv2.destroyWindow("P2")


def sendwebcam():
        print("FILE SEND MODE: Enabled")
        filePath = './logs/Video'

        filelist = os.listdir(filePath)
        # create a zip archive

        archname = './logs/webcam.zip'
        archive = ZipFile(archname, 'w')
        for file in filelist:
            archive.write(filePath + '/' + file)
            print(str(file))
        archive.close()

        # send size
        archivesize = os.path.getsize(archname)

        # send archive
        with open('./logs/webcam.zip', 'rb') as to_send:
            print("Should have worked.")
# capture()
test2()
# sendwebcam()
# firstattempt()