
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