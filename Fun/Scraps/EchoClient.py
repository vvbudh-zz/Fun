import socket
message = "This is a message."

HOST = 127.0.0.1
PORT = 55555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientToServer
