from socket import *
from csv import *
from threading import *
from Utils.School import School
from Utils.Student import Student
import struct

HOST = ""
PORT = 12346

# 3.128.156.248

main_sock = socket()
clients = []
school = School()
running = True


class Jetson(Thread):
    def __init__(self, conn:socket):
        Thread.__init__(self)
        self.conn = conn
        pass

    def wait_for_reponse(self):
        pass


class User(Thread):
    def __init__(self, conn:socket):
        Thread.__init__(self)
        self.conn = conn
        pass

    def wait_for_request(self):
        pass


class Router(Thread):
    def __init__(self, conn:socket):
        Thread.__init__(self)
        self.sock = conn
        self.sock.listen()
        self.running = True

    def run(self):
        while self.running:
            conn,addr = self.sock.accept()

def login(conn:socket):
    # do login thing
    conn.sendall(struct.pack("B",1))
    data = conn.recv(128).decode().split(',') # gets username / pass and spilts it

    if data[0] == "jet123" and data[1] == "12345": #correct username and password for jetson
        temp = Jetson(conn) #store jetson in temp
        temp.start() # starts jetson thread
        return temp

    elif data[0] == "user123" and data[1]=="12346": #correct usename and password for user
        temp = User(conn)
        temp.start() #starts user thread
        return temp 





if __name__ == '__main__':

    main_sock.bind((HOST,PORT))  # Connect the server to the port
    main_sock.listen(4)

    while running:
        conn,addr = main_sock.accept()
        clients.append(login) #sticks it the return from login into clients

    rounter = Router(main_sock)
    rounter.start()
    





