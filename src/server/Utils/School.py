from Utils.Student import Student
from Utils.Course import Course
import csv


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student): # adds student into student list
        self.students.append(student)
 

    def read(self): #reads the file and puts it into the list
        with open ('people.csv',"r", newline='') as file:
            reader = csv.reader(file, delimiter=',')

            for row in reader: 
                if row[3] == "True":
                    temp = True
                else:
                    temp = False

                thing = Student(str(row[0]),int(row[1]),int(row[2]),temp) #uses the student class to seperate the stuff
                self.students.append(thing) #appends stuff to the list
                     

    def find_student_info(self, name: str): #finds info for studet and return
        for s in self.students:
            if s.name == name:
                return s

    def find_course_info(self, course_name: str): # find info for courses 
        for c in self.courses:
            if c.course_name == course_name:
                return c

    def write(self): #writes the info in the list back into the file
        with open ('people.csv', "w", newline='') as file:
            writer = csv.writer(file,delimiter=',')

            for s in self.students: #think of the list as a container and s is for rows, so it writes out info in list
                writer.writerow(s.full_to_csv()) #writes onto file

    def remove_student(self, student): # yeets student into space
        #temp = self.students.index(student)
        self.students.remove(student)
        pass

    def add_course(self, course): # adds course 
        self.courses.append(course)
        pass

    def remove_course(self,course): # yeets course into space
        temp = self.courses.index(course)
        self.courses.remove(temp)
        pass

