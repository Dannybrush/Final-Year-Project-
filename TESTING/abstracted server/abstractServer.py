import socket


class Server:
    def __init__(self, ip, port, buffer_size):
        self.IP = ip
        self.PORT = port
        self.BUFFER_SIZE = buffer_size
        self.connections = []  # connections list
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def startServer(self):
        self.server.bind((self.IP, self.PORT))
        self.server.listen(1)

        self.acceptConnections()

    def acceptConnections(self):
        print("Server: ", self.IP)
        print("*** Listening for incoming connections ***")

        self.client_socket, self.address = self.server.accept()
        print(f"*** Connection from {self.address} has been established! ***")
        self.connections.append(self.client_socket)

        self.progress()
        # # print("hello worlds")

    
    def progress(self):
        
        print("This was 100% successful")
        input()
        message = "Hello and Welcome".encode()
        self.client_socket.send(message)
        input("Sent")
        self.basicfilesend()
        with open("./logs/datafile.txt", "r") as targetfile:
            print(targetfile.read())
        input("hold")
        input("hold")
        input("hold")
        input("hold")

    def disconn(self):
        self.close()
        print("*** Killed")

    def basicfilesend(self):
        path = input("[+] Enter file path: ") # path = "./logs/filesendtst.txt"
        self.client_socket.send(path.encode())
        TFile = self.client_socket.recv(self.BUFFER_SIZE)

        with open("./logs/datafile.txt", "wb+") as targetfile:
            targetfile.write(TFile)



def main():
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
    server.client_socket.send(message)


if __name__ == "__main__":
    main()
