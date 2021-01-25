import socket
import sys
import os
import time


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
        self.server.listen(1)

        self.acceptConnections()

    def acceptConnections(self):
        print(self.IP)
        print("*** Listening for incoming connections ***")

        self.client_socket, self.address = self.server.accept()
        print(f"*** Connection from {self.address} has been established! ***")
        self.connections.append(self.client_socket)
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
    PORT = int(input("[+] Listen on port> "))
    BUFFERSIZE = 2048

    server = Server(IP, PORT, BUFFERSIZE)

    try:
        server.startServer()
    except Exception as e:
        print("*** Error while starting the server:", str(e) + " ***")




if __name__ == "__main__":
    main()
