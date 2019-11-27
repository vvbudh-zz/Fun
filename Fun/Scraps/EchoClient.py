import socket


def communicateToServer():
    """This function communicates to the server sending 10
    pieces of data. That data is "The local variable below. It will also wait
    for recieving data"""
    message = input("Hey what do you want to send to the other computer?")
    i = 0
    HOST = '127.0.0.1'
    #HOST2 = socket.gethostbyname()
    PORT = 55555

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        print("Line is open. s.connect!")

        s.send(message.encode(encoding='utf-8', errors='strict'))
        i = i + 1

        print("Encoded and sent ",i)

        incomingMessage = s.recv(1024)

    print(incomingMessage)


def mainMenu():
    ''' stayon = True while stayon == True:'''
    '''for i in range(0,10):print("\n")'''
    print("Yo, here's the menu options for tonight.")
    print("1 send 1 data packet. \n 0 exit the program.")
    menuSelection = input("Pick your poison.")
    if menuSelection == 1:
        communicateToServer()
    if menuSelection == 0:
        stayon = False



################################################################################
#mainMenu()
communicateToServer()


