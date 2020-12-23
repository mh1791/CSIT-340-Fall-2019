from socket import *
import threading

def ALLCAPS(connection_socket, client_address):
    while True:
        sentence = connection_socket.recv(1024).decode()
        if sentence == "Quit":
            connection_socket.close()
            print("Client connection ended: ", client_address)
            break
        capitalizedSentence  = sentence.upper()
        print(capitalizedSentence)
        connection_socket.send(capitalizedSentence.encode())


class Threads(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("New client connection: ", clientAddress)

    def run(self):
        ALLCAPS(connectionSocket, clientAddress)



serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")

while True:
    connectionSocket, clientAddress = serverSocket.accept()
    t = Threads()
    t.start()
