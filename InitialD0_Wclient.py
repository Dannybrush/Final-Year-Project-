import os
import socket


class Client:
    def __init__(self, server_ip, port, buffer_size, client_ip):
        self.SERVER_IP = server_ip
        self.PORT = port
        self.BUFFER_SIZE = buffer_size
        self.CLIENT_IP = client_ip

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self):
        self.client.connect((self.SERVER_IP, self.PORT))

    def reciept(self):
        while True:
            message = self.client.recv(self.BUFFER_SIZE).decode()
            print("Server:", message)
            # self.send(output.encode())
            self.client.send("[+] Message displayed and closed.".encode("utf-8"))

    def endless(self):
        while True:

            msg = self.client.recv(self.BUFFER_SIZE).decode("utf-8")
            if msg == "msg":
                # self.msg()
                 print("This is where it reached")
            else:
                print("msg = " + msg)


def main():
    SERVER_IP = "192.168.56.1"  # modify me
    PORT = 1337  # modify me (if you want)
    BUFFER_SIZE = 2048

    try:
        os.mkdir('./logs')
    except FileExistsError:
        pass

    CLIENT = socket.gethostname()
    CLIENT_IP = socket.gethostbyname(CLIENT)
    print(CLIENT_IP)
    client = Client(SERVER_IP, PORT, BUFFER_SIZE, CLIENT_IP)

    client.connectToServer()
    client.endless()


if __name__ == "__main__":
    main()
