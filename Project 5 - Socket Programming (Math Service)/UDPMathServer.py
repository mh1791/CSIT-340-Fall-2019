from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive.")

while True:
    expression, clientAddress = serverSocket.recvfrom(2048)
    print("New client request from: ", clientAddress)
    try:
        solution = str(eval(expression))

    except (SyntaxError, NameError):
        solution = "Invalid Input. Enter a valid input or type quit to quit"
    print(solution)
    serverSocket.sendto(solution.encode(), clientAddress)

serverSocket.close()
print("Client connection closed: ", clientAddress)
