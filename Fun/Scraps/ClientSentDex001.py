import socket
x = 0 #This is to prevent the infinite loop
HOST = '127.0.0.1'
PORT = 55555



#This creates the client socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the server.
try:
    serverSocket.bind(('127.0.0.1', 55555))
except Exception as exception:
    print("Failed to connect to server \n", exception)

while x < 10:
    serverSocket, serverAddress = serverSocket.accept()
    #this is the data that will be sent to the server.
    data = x

    #Send the data above to the server and encode it as utf-8
    serverSocket.send(bytes(data))

    #Recieve data from the server
    dataFromServer = serverSocket.recv(1024)
    x = data + 1#incriment x so no infinite loop. Don't want to clog bandwidth.

    print(dataFromServer)