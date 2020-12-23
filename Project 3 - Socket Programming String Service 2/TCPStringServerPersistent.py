from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")
while True:
    connectionSocket, clientAddress = serverSocket.accept()
    print("New client connected: ", clientAddress)
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if sentence == "Quit":
            print("Client connection ended: ", clientAddress)
            connectionSocket.close()
            break
        capitalizedSentence  = sentence.upper()
        print(capitalizedSentence)
        connectionSocket.send(capitalizedSentence.encode())
