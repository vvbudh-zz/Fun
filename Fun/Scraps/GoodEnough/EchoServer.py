import socket
import time




def mainMenuServer():
    selection = input("Yo, this is the server. \n Would you like me to start "
               "listening? Press 1 for yes 0 for no and to exit.")
    if selection == 1:
        startServer()
    else:
        print("This is the end of the server as we know it. Good night!")

def startServer():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 55555  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        # conn, addr = s.accept()  # Establish connection with client.
        with conn:
            print('Connected by', addr)
            while conn:
                incomingMessage = conn.recv(1024).decode(encoding='utf-8',
                                                         errors='strict')
                print(incomingMessage)
                print("\nReceipt of message, Closing connection.")
            conn.send("Receipt of message, Closing connection.")
            conn.close()


mainMenuServer()







