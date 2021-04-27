import os
import socket
import time


class Client:
    def __init__(self, server_ip, port, buffer_size, client_ip):
        self.SERVER_IP = server_ip
        self.PORT = port
        self.BUFFER_SIZE = buffer_size
        self.CLIENT_IP = client_ip
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self):
        self.client.connect((self.SERVER_IP, self.PORT))
        
    def progress(self):
        flag = True
        while flag:
            input("Client Connected")
            message = self.client.recv(1024).decode()
            # message = self.client.recv(1024).decode()
            # print(message.decode())
            print(message)
            input("Received")
            with open("./logs/filesendtst.txt", 'w+') as write:
                write.write("HERE IS A TEXT FILE THAT HAS BEEN WRITTEN WITH THE INTENTION OF SENDING AND RECEIVING")
            self.filereceive()
            input("hold")
            input("hold")
            input("hold")
            input("hold")

    def filereceive(self):

        while True:
            try:
                path = self.client.recv(self.BUFFER_SIZE).decode()
                #path = input("[+] Enter file path: ") # path = "./logs/filesendtst.txt"

                if not os.path.exists(path):
                    raise FileNotFoundError
                else:
                    break
            except FileNotFoundError:
                print("[!] File not found, retry")

        with open(path, 'rb') as to_send:
            print("opened")
            data = to_send.read()
            self.client.send(data)
        print("*** File sent ***")

def main():
    SERVER_IP = "192.168.56.1"  # modify me
    PORT = 1337  # modify me (if you want)
    BUFFER_SIZE = 2048

    CLIENT = socket.gethostname()
    CLIENT_IP = socket.gethostbyname(CLIENT)
    print("Client: ", CLIENT_IP)
    client = Client(SERVER_IP, PORT, BUFFER_SIZE, CLIENT_IP)

    client.connectToServer()
    client.progress()


if __name__ == "__main__":
    main()
