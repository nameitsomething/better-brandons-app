from socket import *
from csv import *
import threading

HOST = ""
PORT = 12346

main_sock = socket()
clients =[]


class People(self):
    people = []

    with open ('list.csv', newline=' ') as file:
        reader = csv.reader(file, delimiter=',')

        for row in reader:
            people.append(row)

        print(people)




class Router(Thread):
    def __init__(self, conn:socket):
        Thread.__init__(self)
        self.sock = conn
        self.sock.listen()
        self.running = True

    def run(self):
        while self.running:
            conn,addr =self.sock.accept()
            session = Session(conn)
            if session not in clients: #adds new session
                session.start()
                clients.append(session)



if __name___ == '__main__':
    main_sock.bind((HOST,PORT))
    router = Router(main_sock)
    router.start()
    People.start()


