import ctypes
import os
import subprocess
import time

import pyperclip


def locksystem():
    msg = "rundll32.exe user32.dll, LockWorkStation"
    runrun(msg)


def shutdown():
    msg = "shutdown /s"
    runrun(msg)


def shutdownmessage():
    msg = "shutdown /s /e 'You've been hacked '"
    runrun(msg)


def restart():
    msg = "shutdown /r"
    runrun(msg)

def playchess():
    msg = "start /B start cmd.exe @cmd /c telnet freechess.org "
    runrun(msg)
    # chess_true = subprocess.check_call("start /B start cmd.exe @cmd /k telnet freechess.org ", shell=True)
def playstarwars():
    msg = "start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl "
    runrun(msg)
    # Sw = subprocess.check_call("start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl ", shell=True)
def weather():
    msg = "start /B start cmd.exe @cmd /c telnet rainmaker.wunderground.com "
    runrun(msg)
    # weather = subprocess.check_call("start /B start cmd.exe @cmd /c telnet rainmaker.wunderground.com ", shell=True)
# def starwars():
#     msg = "telnet towel.blinkenlights.nl"
#     try:
#         runprocess(msg)
#         #newtest(msg)
#     except:
#         print("telnet must be enabled")
#
# def thirdtest():
#     print("Thirdtest")
#     msg = "telnet towel.blinkenlights.nl"
#     try:
#         #Id = subprocess.check_output([msg], check=True).decode('utf-8').split('\n')
#         os.system("start /B start cmd.exe @cmd /k telnet towel.blinkenlights.nl")
#     except:
#         print("failed")
#
#
# def newtest(msg):
#     Id = subprocess.check_output(msg).decode('utf-8').split('\n')
#     new = []
#
#     # arrange the string into clear info
#     for item in Id:
#         new.append(str(item.split("\r")[:-1]))
#     for i in new:
#         print(i[2:-2])
#
#
# def runprocess(msg):
#     try:
#         obj = subprocess.Popen(msg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
#                                shell=True)
#         output = (obj.stdout.read() + obj.stderr.read()).decode("utf-8", errors="ignore")
#         print("A")
#     except subprocess.CalledProcessError:
#         print("RunProcess Failed")
#         output = "Failed"
#     except Exception:
#         print("unknown err")
#
#     if output == "" or output == "\n":
#         print("B")
#     else:
#         print("C" + str(output.type))
#
# def runCommand():
#     try:
#         subprocess.Popen(["pkgmgr", "/iu:”TelnetClient”"], shell=True)
#     except Exception as e:
#         print("This failed too : " + str(e))
#
#
# def TN():
#     try:
#         telnet_enabled = subprocess.check_call("start /B start cmd.exe @cmd /c pkgmgr /iu:TelnetClient ", shell=True)
#         print("Telnet Enabled Successfully")
#
#     except subprocess.CalledProcessError:
#         print("ERR Enabling Telnet")
#     print(str(telnet_enabled))
#
# def enabletelnet():
#     os.system("start /B start cmd.exe @cmd /c pkgmgr /iu:TelnetClient ")

def runprocess(msg):
    obj = subprocess.run(msg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                         shell=True)
    output = (obj.stdout.read() + obj.stderr.read()).decode("utf-8", errors="ignore")
    print("A")
    if output == "" or output == "\n":
        print("B")
        # self.client.send("[*] Done".encode("utf-8"))
    else:
        print("C")
        # self.client.send(output.encode("utf-8"))

def runrun(msg):
    obj = "failed"
    try:
        obj, _ = subprocess.run(msg, check=True, shell=True)
        #output = (obj.stdout.read() + obj.stderr.read()).decode("utf-8", errors="ignore")
    except Exception as e:
        print("This failed too (runrun) : " + str(e) + " + " + str(obj))

def MSGBOX():

    insert = "this is a test"

    msgA = '(echo MsgBox "'+insert+'" ^& vbCrLf ^& "Line 2",262192, "Title")> File.vbs'
    runrun(msgA)
    msgB = 'start File.vbs'
    runrun(msgB)


def ctypesmsgbox():
    msg = "testmessage"
    ctypes.windll.user32.MessageBoxW(0, f"{msg}", 'Alert!', 0)

def enableTN():
    msg = "start /B start cmd.exe @cmd /c pkgmgr /iu:TelnetClient "
    runrun(msg)
input()
#TN()
#enableTN()

#print("telnet")
#print("TT")
#time.sleep(20)
#playchess()
#playstarwars()
#weather()
#for i in range(0, 10):
#    print(i)
#locksystem()
#MSGBOX()
#ctypesmsgbox()

def execfile():
    path2script = input("type starwars.py")
    print("HERE ")
    try:
        exec(open(path2script).read())
        print("SUCCESS")
    except FileNotFoundError as fnfe:
        print("FAILURE " + str(fnfe))
    except Exception as e:
        print("FAILURE " + str(e))


def clipboard():
    cb = pyperclip.paste()  # getting the clipboard

    if len(cb) == 0:
        print("/No Clipboard contents/")
    else:
        print(cb)


for i in range(10):
    clipboard()
    time.sleep(5)

passwordpasswordpassword