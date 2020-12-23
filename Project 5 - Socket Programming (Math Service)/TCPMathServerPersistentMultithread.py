from socket import *
import threading

def evaluate_expression(connection_socket, client_address):
    while True:
        expression = connection_socket.recv(1024).decode()
        if expression == "quit":
            connection_socket.close()
            print("Client connection closed: ", client_address)
            break
        try:
            solution = str(eval(expression))
        except (SyntaxError, NameError):
            solution = "Invalid Input. Enter a valid input or type quit to quit"
        print(solution)
        connection_socket.send(solution.encode())


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("New client connection: ", clientAddress)
    def run(self):
        evaluate_expression(connectionSocket, clientAddress)



serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")


while True:
    connectionSocket, clientAddress = serverSocket.accept()
    t = MyThread()
    t.start()
