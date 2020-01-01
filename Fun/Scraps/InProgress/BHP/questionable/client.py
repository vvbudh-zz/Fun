'''Program idea 1.
Make a program that opens 3 sockets and sends three pieces of data.
the server must add these pieces of data up and then return the data.'''

import random as rand
import socket
#Target Host and Target Port
th01 = "www.example.com"
tp01 = 2221
tp02 = 2222
tp03 = 2223

#create the socket object
#Args, what kind of socket?
socket01 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket02 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket03 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#Connect the client to the server.
socket01.connect(th01, tp01)
socket02.connect(th01, tp02)
socket03.connect(th01, tp03)


#send some data.
socket01.send((rand.randint)).encode('utf-8')
socket02.send((rand.randint)).encode('utf-8')
socket03.send((rand.randint)).encode('utf-8')
