'''This program will open a file and add words to it
depending on what the user wants to type in.
It will also send the data via UDP to a listening NetCat
server and then close the connection.
The program should also handle the exception if the server
isn't actually turned on it should still exit "gracefully"'''
import socket
import os
import io
import os

# This is the socket code
'''     
#This is the socket code.
    
#This is the ip of the Target.
IPADDR = "192.168.254.77"
#Random port
PORT = 16515

#This is the data for the UDP Packet. The ".decode('hex) is super
# important because without it it won't be sent in hex like all other
# network traffic is and will not output what you wanted it to."
PACKETDATA = 'f1a525da11f6'.decode('hex')


#This initializes the socket, think of this as a cable.
#SOCK_DGRAM designates this as UDP.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

#This is the exception block. Try these lines of coif
try:
    #Connects the socket,
    #This is like a cable to the address location
    s.connect((IPADDR, PORT))

    #send the data of PACKETDATA
    s.send(PACKETDATA)
#This says just do whatever man. Keep goin even if it fails.
except:
    pass


#This ends the connection and closes the socket.
s.close()


#This is the end of the socket code.
'''
# This is the end of the socket code.

# This opens the file we want to read and the variable is called
# file1. That's the designation is for the file.
'''with open('test.txt', 'r') as file1:
    #Just the variable to read 100 characters

    sizeToRead = 100
    file1Contents = file1.read(sizeToRead)

   # while len(file1Contents) > 0:
        print(file1Contents, end='*')
        file1Contents = file1.read(sizeToRead)'''


def makeFileGus():
    '''This function creates the base test file'''
    with open('Gus.txt', 'w') as file1:
        file1.write(
            "Virgil I. Grissom, in full Virgil Ivan Grissom, byname Gus "
            "Grissom, (born April 3, 1926, Mitchell, Ind., U.S.—died Jan. "
            "27, 1967, Cape Kennedy, Fla.), second U.S. astronaut to "
            "travel in space and the command pilot of the ill-fated "
            "Apollo 1 crew. He and his fellow astronauts Edward H. "
            "White and Roger B. Chaffee were killed, becoming the "
            "first casualties of the U.S. space program, when a flash "
            "fire swept their space capsule during a simulation of the "
            "scheduled Feb. 21, 1967, launching of Apollo 1."
            "\n\nCommissioned in the U.S. Air Force in 1951, Grissom "
            "flew 100 missions in the Korean War, earning the "
            "Distinguished Flying Cross and the Air Medal with cluster. "
            "He was a test pilot and flying instructor until 1959, when "
            "he was selected as one of the original seven astronauts for "
            "Project Mercury. On July 21, 1961, with a 15-minute "
            "suborbital journey aboard the space capsule Liberty Bell 7, "
            "Grissom became the third man to enter space. Upon "
            "splashdown, the explosive bolts of the capsule’s hatch "
            "unexpectedly opened, and Grissom immediately had to leave "
            "Liberty Bell 7, which sank in more than 4,500 metres "
            "(15,000 feet) of water. \n\n On March 23, 1965, Grissom "
            "became the first man to return to space as he "
            "(as command pilot) and Lieutenant Commander John W. "
            "Young made three orbits in the first manned Gemini flight, "
            "Gemini 3. During that flight Grissom demonstrated that a "
            "space capsule could be maneuvered manually.")


def readFileGus():
    with open("Gus.txt", 'r') as file1:
        print(file1.read())


def main():
    # makeFileGus()
    readFileGus()


main()
