#Take in three sockets worth of data and add them and pass them back.
import socket
import threading


bind_ip = "127.0.0.1"
bp01 = 2221
bp02 = 2222
bp03 = 2223

#Making the sockets
lSocket01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lSocket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lSocket03 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#this sets them to the ports they need to be set at.
lSocket01.bind((bind_ip,bp01))
lSocket02.bind((bind_ip,bp02))
lSocket03.bind((bind_ip,bp03))

#this does what it says.
lSocket01.listen(5)
lSocket02.listen(5)
lSocket03.listen(5)


print ("Listening on %s:%d " % (bind_ip,bp01), "-3")

'''def handle_client(lSock01, lSock02, lSock03):
    """This is supposed to handle all three sockets at the same time."""
    #print out what the client sent us.
    int1 = lSock01.recv()
    int2 = lSock02.recv()
    int3 = lSock03.recv()

    sum = int1 + int2 + int3

    print("[*] Recieved 3 sum %q" % sum)

    #send back a packet.
    lSock01.send("ACK!")
    lSock02.send("ACK!")
    lSock03.send("ACK!")

    #close the connections.
    lSock01.close()
    lSock01.close()
    lSock01.close()'''


while True:
    client,addr = lSocket01.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    #spin up client thread to handle incoming data?
    #What do you mean spin up? IT's a socket. It opens. Dumbass lol jk
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()