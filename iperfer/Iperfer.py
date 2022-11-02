import socket
import sys, getopt
import time
import threading

size = 1000
FORMAT = 'utf-8'
mode = ""
DISCONNECT_MESSAGE = "!DISCONNECT"
host = ""
port = ""
tim = 0

def send(msg):
    message = str(msg).encode(FORMAT)
    if msg == "":
        message += b'0' * 1000
    client.send(message)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    global servercount, tim, rate
    servercount = 0
    start = time.time()

    connected = True
    while connected:
        msg = conn.recv(size).decode(FORMAT)
        if msg:
            servercount += 1
        else:
            servercount = servercount - 1
            connected = False
    
    now = time.time()
    tim = now - start
    rate = round(servercount / (1024 * tim), 3)
    print(f"received={servercount} kb rate={rate} Mbps")
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {host}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

opts = ""
args = ""
portnumber_error = False
try:
    opts, args = getopt.getopt(sys.argv[1:],"csh:p:t:")
except:
    print("Error: missing or additional arguments")
if opts != "" and args != "":
    for opt, arg in opts:
        if opt in ['-c']:
            mode = "client"
        elif opt in ['-s']:
            mode = "server"
        elif opt in ['-h']:
            host = arg
        elif opt in ['-p']:
            port = int(arg)
        elif opt in ['-t']:
            tim = int(arg)

    if mode == "":
        print("Error: missing or additional arguments")
    elif port < 1024 or port > 65535:
        print("Error: port number must be in the range 1024 to 65535")
        portnumber_error = True
    elif mode == "client":
        if host == "" or port == "" or tim == 0:
            print("Error: missing or additional arguments")
    elif mode == "server":
        if port == "":
            print("Error: missing or additional arguments")

if not portnumber_error:
     if mode == "client" and host != "" and port != "" and tim != 0:
            addr = (host, port)
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(addr)
            clientcount = 0
            sendata = ""
            rate = 0
            end = time.time() + etime

            while time.time() <= end:
                send(sendata)
                clientcount += 1

            rate = round(clientcount / (1024 * etime), 3)

            send(DISCONNECT_MESSAGE)

            print(f"sent={clientcount} kb rate={rate} Mbps")

     
     
     elif mode == "server" and port != "":
            addr = (host, port)
            host = socket.gethostbyname(socket.gethostname())
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(addr)
            servercount = 0
            print("[STARTING] server is starting...")
            start()	
