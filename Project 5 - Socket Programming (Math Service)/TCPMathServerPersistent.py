from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print("The server is ready to receive.")

while True:
    connectionSocket, clientAddress = serverSocket.accept()
    print("New client connection: ", clientAddress)
    while True:
        expression = connectionSocket.recv(1024).decode()
        if expression == "quit":
            connectionSocket.close()
            print("Client connection closed: ", clientAddress)
            break
        try:
            solution = str(eval(expression))
        except (SyntaxError, NameError):
            solution = "Invalid Input. Enter a valid input or type quit to quit"

        print(solution)
        connectionSocket.send(solution.encode())
