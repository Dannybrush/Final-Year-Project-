import socket

class Client:
    def __init__(self, server_ip, port, buffer_size, client_ip):
        self.SERVER_IP = server_ip
        self.PORT = port
        self.BUFFER_SIZE = buffer_size
        self.CLIENT_IP = client_ip
        # self.recvcounter = 0


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
def main():
    SERVER_IP = "192.168.56.1"  # modify me
    PORT = 1337  # modify me (if you want)
    BUFFER_SIZE = 2048

    CLIENT = socket.gethostname()
    CLIENT_IP = socket.gethostbyname(CLIENT)
    print(CLIENT_IP)
    client = Client(SERVER_IP, PORT, BUFFER_SIZE, CLIENT_IP)

    client.connectToServer()
    client.progress()


if __name__ == "__main__":
    main()
