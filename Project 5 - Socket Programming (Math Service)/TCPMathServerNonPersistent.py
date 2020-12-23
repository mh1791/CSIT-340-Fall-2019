from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")

while True:

    connectionSocket, clientAddress = serverSocket.accept()
    print("New client request from: ", clientAddress)

    expression = connectionSocket.recv(1024).decode()

    try:
        solution = str(eval(expression))

    except (SyntaxError, NameError):
        solution = "Invalid Input. Enter a valid input or type quit to quit"

    print(solution)

    connectionSocket.send(solution.encode())
    connectionSocket.close()
    print("Client connection closed: ", clientAddress)
