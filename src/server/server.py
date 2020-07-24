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

    def run(self)-> None:
        pass


class User(Thread):
    def __init__(self, conn:socket):
        Thread.__init__(self)
        self.sock = conn
        self.running = True
        print("Created User Thread")
        school.read()
        pass

    def wait_for_request(self):
        # recv a command

        data = self.sock.recv(128).decode().split(",") # Decode
        command = int(data[0]) # locate command and yionks it
        print(command)
        

        if command == 2: # decide, send student info command
            print("in there")
            print(data[1])
            self.sock.sendall(school.find_student_info(data[1]).full_to_bytes()) # respond
            print("sent full student info")

        elif command == 3: #ask for course info and sends course ingo
            self.sock.sendall(school.find_course_info(data[1]).to_bytes()) #yeets the course info
            print("sent course data")

        elif command == 4: # add student
            school.add_student(data[1])

        elif command == 5: #remove student
            school.remove_student(data[1])

        elif command == 6: #  remove student by name
            school.remove_student_by_name(data[1])

        elif command == 7: #remove student by numbers
            school.remove_student_by_number(data[1])

        elif command == 8: #add course
            school.add_course(data[1])

        elif command == 9: #remove course
            school.remove_course(data[1])

        elif command == 10: #remove course by name
            school.remove_course_by_name(data[1],data[2])

        elif command == 11: #remove course by number
            school.remove_course_by_number(data[1],data[2])

        elif command == 12: #add student to course
            school.add_student_to_course(data[1],data[2])

        elif command == 13: #add student to course by name
            school.add_student_to_course_by_name(data[1],data[2],data[3])

        elif command == 14: #add student to course by number
            school.add_student_to_course_by_number(data[1],data[2],data[3])

        elif command == 15: #remove student from course
            school.remove_student_from_course(data[1],data[2])

        elif command == 16: #remove student from course by name
            school.remove_student_from_course_by_name(data[1],data[2],data[3])

        elif command == 17: #remove student from course by number
            school.remove_student_from_course_by_number(data[1],data[2],data[3])

        elif command == 18: #check in student
            school.check_in_student(data[1])

        elif command == 19: #check in student by name
            school.check_in_student_by_name_(data[1])

        elif command == 20: #check in student by number
            school.check_in_student_by_number(data[1])

        elif command == 21: #check out student
            school.check_out_student(data[1])

        elif command == 22: #check out student by name
            school.check_out_student_by_name_(data[1])

        elif command == 23: #check out student by number
            school.check_out_student_by_number(data[1])

        elif command == 24: #send all school info
            student = school.send_student_info()
            course = school.send_course_info()
            self.sock.sendall(str.encode(f"{len(student)},{len(course)}"))

            for s in student:
                temp =f"{s}"
                self.sock.sendall(str.encode(temp))

            for c in course:
                temp = f"{c}"
                self.sock.sendall(str.encode(temp))



        elif command == 66: #murder the server and yeet everything into oblvion and yeetus yourself
            self.running = False
            self.sock.detach()
            exit(0)

        elif command == 100: # kill user 
            self.running = False
            # send kill sig to user

    def run(self)->None:
        while self.running:
            try:
                self.wait_for_request()
            except timeout as tim:
                print(tim)
        self.sock.detach()


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
        print("new user")
        return temp 
    else:
        print("nope")


if __name__ == '__main__':

    main_sock.bind((HOST,PORT))  # Connect the server to the port
    main_sock.listen(4)

    while running:
        conn,addr = main_sock.accept()
        clients.append(login(conn)) #sticks it the return from login into clients
    





