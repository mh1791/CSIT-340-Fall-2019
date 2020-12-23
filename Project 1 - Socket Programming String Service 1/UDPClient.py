from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = input("Input a lowercase sentence: ")
    if message == "Quit":
        clientSocket.close()
        break
    else:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
