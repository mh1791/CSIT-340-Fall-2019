from socket import *

serverHost = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

while True:

    expression = input("Input a basic expression: ")
    clientSocket.send(expression.encode())
    if expression == "quit":
        break
    solution = clientSocket.recv(1024)

    print(solution.decode())
clientSocket.close()
