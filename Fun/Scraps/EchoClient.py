import socket
packetCounter = 0

MESSAGE = "This is a complete sentence."

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 55555        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.send(bytes(packetCounter))
    incomingData = s.recv(1024)
packetCounter = ord(incomingData)
print('Received', repr(incomingData))