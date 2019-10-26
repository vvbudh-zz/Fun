import os
import sys
import socket
import subprocess as sub
#https://www.youtube.com/watch?v=TMbHg43as_E&list=PLhTjy8cBISErYuLZUvVOYsR1giva2payF&index=8

#Creating a socket "connect two PCs"
def createSocket():
    try:
        #Defining the variables here. Making global for some reason.....
        global host #Host IP
        global port #Port #
        global socket  #Socket

        #nothing in host right now because this is "Server.py" It'll likely be localhost.
        host = ""
        port = 23345
        s = socket.socket()

    except socket.error as msg:
        print("Socket failed to create." + str(msg))

#binding socket and listening for connections.
def bindSocket():
        try:
            global host
            global port
            global socket

            print ("Executing bindSocket()" + str(port))

            #this is the function that will bind the port.
            s.bind((host,port))
            s.listen(5)

        except socket.error as msg:
                print("The socket failed to bind " + str(msg) + "/n" + "Retrying now.")
                #this is recursion, We're retrying by redoing the function.
                bindSocket()

#Establish connection with the client. (Socket must be listening)

def socketAccept():
    conn,address = s.accept()
    print("Connection established " + "IP:"+ address[0] + "Port:" +str(address[1]))
    transmit(conn)
    conn.close()

def transmit(conn):
    #https://www.youtube.com/watch?v=JT0WaoHR0TI&list=PLhTjy8cBISErYuLZUvVOYsR1giva2payF&index=11
