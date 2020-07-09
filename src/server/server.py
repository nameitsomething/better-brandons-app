from socket import *
from csv import *
from threading import *

HOST = ""
PORT = 12346

main_sock = socket()
clients = []

class present:
    def __init__(self,name,age,grade,present):
        self.name = name
        self.age = age
        self.grade = grade
        self.present = present


class People:
    def __init__(self):
        self.students = []

    def read(self):
        with open ('people.csv',"r", newline=' ') as file:
            reader = csv.reader(file, delimiter=',')

            for row in reader:
                thing = present(row[0],row[1],row[2],row[3])
                students.append(thing)
                print(thing)     

    def write(self):
        with open ('people.csv', "w", newline='') as file:
            writer = csv.writer(file,delimiter=',')

            for s in self.students:
                writer.writerow(s)
                print(s)


class Jetson_Client(Client):  # Will interface with the jetson
    pass

class User_Client(Client):  # Will interface with the client app
    pass

class Client(Thread):
    def __init__(self, )


class Router(Thread):
    def __init__(self, conn:socket):
        Thread.__init__(self)
        self.sock = conn
        self.sock.listen()
        self.running = True

    def run(self):
        while self.running:
            conn,addr = self.sock.accept()



if __name__ == '__main__':

    main_sock.bind((HOST,PORT))  # Connect the server to the port
    main_sock.listen(0)

    rounter = Router(main_sock)
    rounter.start()

    test = People()
    test.read()
    test.write()





