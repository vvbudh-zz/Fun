import socket
import time

def communicateToServer():
    """This function communicates to the server sending 10
    pieces of data. That data is "The local variable below. It will also wait
    for recieving data###No it doesn't. It just starts off with sending the
    data then it asks if you'd like to try again or returns you to the main
    menu."""
    message = input("Hey what do you want to send to the other computer?\n")
    i = 0
    HOST = '127.0.0.1'
    #HOST2 = socket.gethostbyname()
    PORT = 55555

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        print("Line is open. s.connect!\n")

        s.send(message.encode(encoding='utf-8', errors='strict'))
        i = i + 1
        print("Total messages sent -> ", i, "\n")
        #mostly flavor text here to make it easier on the user.
        print("Encoded and sent this message ->", message)
        #Trying to get the selection to be the menu options just like in my
        # C++ programs.
        selection = input("Would you like to send another message? 1 for yes, "
                          "2 for listen, or 0 for no. \n")
        #This is the ending of the function. It asks if you'd like to
        # continue again or return to the main menu.
        if selection == 1:
            communicateToServer()
        elif selection == 2:
            listen()
        else:
            print("The end.")

def listen()
    """This is going to be the listen program, all it does is activate when
    the client wants to listen to the server to recieve data."""
    incomingMessage = s.recv(1024).decode(encoding='utf-8',
                                             errors='strict')



def mainMenu():
    ''' This is the main menu. This should hold most of the programs
    and most of the other cool applications I create.'''
    '''for i in range(0,10):print("\n")'''
    print("Yo, here's the menu options for tonight.")
    print("1 to execute Communicate To Server! \n 0 to EXIT the program.")
    menuSelection = input("Pick your poison.")
    if menuSelection == 1:
        communicateToServer()
    if menuSelection == 0:
        stayon = False



################################################################################
#mainMenu()
communicateToServer()


