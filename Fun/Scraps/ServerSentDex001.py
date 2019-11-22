import socket
import sys
HOST = '127.0.0.1'
PORT = 55555

HEADDERSIZE = 100 #This is the headder size a CONSTANT for the program.

#Sock Stream = TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#This binds the socket to the localhost.

#Bind and listen.
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)#This is a queue. Too many TCP packets coming in this will hold 5.

countIncriment = 0 #This is going to be the end number of
# packets/interactions between the server and the client.

#Accept Connections.
#This accepts any connection forever.
while True:
    (clientSocket, clientAddress) = serverSocket.accept()
#What's the f for? {address}
    print("Accepted a connection request from %s:%s"%(clientAddress[0],
                                                      clientAddress[1]))

    #recieve data from client
    dataFromClient = clientSocket.recv(1024)

    clientSocket.send(bytes(countIncriment))

