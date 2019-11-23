import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 55555        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listenSocket:
    listenSocket.bind((HOST, PORT))
    listenSocket.listen()
    outsideConnection, addr = listenSocket.accept()

    with outsideConnection:
        print('Connected by', addr)
        while True:
            data = int(outsideConnection.recv(1024))
            if not data:
                break
            data = data + 5
            outsideConnection.send(bytes(data))
            #outsideConnection.sendall(data)#send the data back to the client
            print(data)