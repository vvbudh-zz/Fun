import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 55555        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    #conn, addr = s.accept()  # Establish connection with client.
    with conn:
            print('Connected by', addr)
            while conn:
                incomingMessage = conn.recv(1024).decode(encoding='utf-8',
                                                          errors='strict')
                print(incomingMessage)
            conn.send("Receipt of message, Closing connection.")

