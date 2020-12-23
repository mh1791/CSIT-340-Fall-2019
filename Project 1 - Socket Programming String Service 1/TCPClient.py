from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:
    sentence = input("Input a lowercase sentence: ")
    if sentence == "Quit":
        clientSocket.close()
        break
    else:
        serverName = 'localhost'
        serverPort = 5000
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print(modifiedSentence.decode())