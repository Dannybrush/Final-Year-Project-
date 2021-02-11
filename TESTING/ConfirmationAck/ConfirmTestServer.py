import socket
# import sys
import os
import time
import random
import string


class Server:
    def __init__(self, ip, port, buffer_size):
        self.IP = ip
        self.PORT = port
        self.BACKUP_PORT = 8080
        self.BUFFER_SIZE = buffer_size

        self.connections = []  # connections list
        self.info = ""  # info about target
        self.recvcounter = 0  # counter for received files

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def startServer(self):
        self.server.bind((self.IP, self.PORT))
        self.server.listen(2)

        self.acceptConnections()

    def acceptConnections(self):
        print(self.IP)
        print("*** Listening for incoming connections ***")

        self.client_socket, self.address = self.server.accept()
        print(f"*** Connection from {self.address} has been established! ***")
        self.connections.append(self.client_socket)
        # # safemode

        mode = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        print(mode)
        if mode == "2":
            print("Virtuous mode")
            self.connectionconfirm()
        else:
            print("Malicious mode")

        self.progress()
        # # print("hello worlds")

    def generatekey(self):
        # Creates a password containing uppercase, lowercase, numerical digits and punctuation.
        letters = (string.ascii_letters + string.digits + string.punctuation)
        code = ''.join(random.choices(letters, k=10))
        # print("Key =  " + code)
        return code

    def connectionconfirm(self):
        key = self.generatekey()
        print("Key =  " + key)

        self.client_socket.send(key.encode("utf-8"))

        response = self.client_socket.recv(self.BUFFER_SIZE).decode()
        if response == "MISMATCH":
            self.close()

    def progress(self):
        print("This was 100% successful")
        input()

    def disconn(self):
        command = "disconnect"
        self.client_socket.send(command.encode("utf-8"))
        print("*** Killed")


def main():
    """ Creating the necessary dirs """

    try:
        os.mkdir('../receivedfile')
    except FileExistsError:
        pass

    # banner()
    time.sleep(1)

    HOSTNAME = socket.gethostname()
    IP = socket.gethostbyname(HOSTNAME)
    PORT = 1337  # int(input("[+] Listen on port> "))
    BUFFERSIZE = 2048

    server = Server(IP, PORT, BUFFERSIZE)

    try:
        server.startServer()
    except Exception as e:
        print("*** Error while starting the server:", str(e) + " ***")
    # just sending a message, for demonstration purposes
    message = "Hello and Welcome".encode()
    # server.client_socket.send(message)


if __name__ == "__main__":
    main()
