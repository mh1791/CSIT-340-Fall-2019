from socket import *

serverHost = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)

expression = input("Input a basic expression: ")

while expression != "quit":
    
    clientSocket.sendto(expression.encode(), (serverHost, serverPort))
    solution, serverAddress = clientSocket.recvfrom(2048)
    print(solution.decode())
    expression = input("Input a basic expression: ")

clientSocket.close()
