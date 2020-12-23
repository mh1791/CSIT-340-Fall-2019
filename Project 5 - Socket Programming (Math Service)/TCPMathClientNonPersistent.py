from socket import *
serverHost = 'localhost'
serverPort = 5000


expression = input("Input a basic expression: ")

while expression != "quit":

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))
    clientSocket.send(expression.encode())
    solution = clientSocket.recv(1024)
    print(solution.decode())
    clientSocket.close()
    expression = input("Input a basic expression: ")
