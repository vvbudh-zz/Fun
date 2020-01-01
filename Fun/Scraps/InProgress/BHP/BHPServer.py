import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 12700

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))
server.listen(5)

print ("[*] Listening on %s:%d" % (bind_ip,bind_port))

#client-handling thread
def handle_client(client_socket)

    #print out what the client sends
    request = client_socket.recv(1024)
    #The %s is the first variable, you just put the variable in after.
    print ("[*] Recieved: %s" % request)

    #send back a packet.
    client_socket.send("ACK!")

    client_socket.close()

while True:
    client,addr = server.accept()

    print ("[*] Accepted connection from  %a:%b") % (addr[0],addr[1])

    #Spin up our client thread to handle incoming data.
    client_handler - threading.Thread(target=handle_client,args=(client,))
    client_handler.start()