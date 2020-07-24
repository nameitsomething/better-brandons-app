from Utils.Student import Student
from Utils.Course import Course
import csv
from typing import overload


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.student_numbers = 1

    def add_student(self, student): # adds student into student list
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    return False

            student.set_student_number(self.student_numbers)
            self.student_numbers = self.student_numbers + 1

      
            self.students.append(student)
            return True
 
    def send_student_info(self):
        temp = []
        for s in self.students:
            temp.append(s.full_to_csv())

        return temp

    def send_course_info(self):
        temp = []

        for c in self.courses:
            temp.append(c.full_to_csv_course())

        return temp


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

        with open('course.csv',"r",newline='') as file:
            reader = csv.reader(file, delimiter=',')

            for row in reader:
                thing = Course(str(row[0]),str(row[1]),int(row[2]),int(row[3]))
                self.courses.append(thing)
                

    def find_student_info(self, name): #finds info for studet and return
        if name != None:
            for s in self.students:
                if s.name == name:
                    return s
        

    def find_course_info(self, course_name: str): # find info for courses 
        for c in self.courses:
            if c.course_name == course_name:
                return c

    def check_in_student(self, student:Student): #master attendence
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    s.check_in()
                    return True

    def check_in_student_by_name_(self, name):
        if name !=None:
            for s in self.students:
                if s.name == name:
                    s.check_in()
                    return True

    def check_in_student_by_number(self, number):
        if number !=None:
            for s in self.students:
                if s.number == number:
                    s.check_in()
                    return True

    def check_out_student(self, student:Student): #master attendence
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    s.check_out()
                    return True

    def check_out_student_by_name_(self, name):
        if name !=None:
            for s in self.students:
                if s.name == name:
                    s.check_out()
                    return True

    def check_out_student_by_number(self, number):
        if number !=None:
            for s in self.students:
                if s.number == number:
                    s.check_out()
                    return True

    



    def write(self): #writes the info in the list back into the file
        with open ('people.csv', "w", newline='') as file:
            writer = csv.writer(file,delimiter=',')

            for s in self.students: #think of the list as a container and s is for rows, so it writes out info in list
                writer.writerow(s.full_to_csv()) #writes onto file

        with open('course.csv',"w",newline='') as file:
            writer = csv.writer(file,delimiter=',')

            for c in self.courses:
                writer.writerow(c.full_to_csv_course())
    

    def remove_student(self, student): #yeet students in space by student     
        if student != None: 
            for s in self.students:
                if s.name == student.name:
                    for c in self.courses:
                        c.remove_student(s)

                    self.students.remove(s)

    def remove_student_by_name(self, name):               
        if name != None:
            for s in self.students:
                if s.name == name:
                    for c in self.courses:
                        c.remove_student(s)

                    self.students.remove(s)
                    break


    def remove_student_by_number(self, number):
        if number != None:
            for s in self.students:
                if s.student_number == number:
                    for c in self.courses:
                        c.remove_student(s)
                        print("removed student")
                        
                    self.students.remove(s)
                    break


    def add_course(self, course): # adds course 
        if course != None:
            for c in self.courses:
                if course.section == c.section and (course.name == c.name or course.number == c.number):
                    return False
            self.courses.append(course)
            return True
        return False

    def remove_course(self,course: Course = None): # yeets course into space
        for c in self.courses:
            if c.course_name == course.course_name and c.section == course.section:
                self.courses.remove(c)
                print("remove course")
                
    def remove_course_by_name(self, name, section):
        for c in self.courses:
            if c.course_name == name and c.section == section:
                self.courses.remove(c)
                print("course remove")

    def remove_course_by_number(self,number,section):
        for c in self.courses:
            if c.course_number == number and c.section == section:
                self.courses.remove(c)
                print("remove course by num")
    

    def add_time(self):
        pass

    def remove_time(self):
        pass

    def add_student_to_course(self, student: Student, course: Course): #idk why no work
        temp_student = None

        if student != None:
            for s in self.students:
                if s.name == student.name:
                    temp_student = s
                    print("student is now temp")


        if course != None:
            for c in self.courses:
                if c.course_num == course.course_num and c.section == course.section:
                    c.add_student(temp_student)
                    print("added student to course")
                    return True

            return False


    def add_student_to_course_by_name(self,student_name:str,course_name:str, course_section:int):
        temp_student = None
        print(student_name + course_name)
        if student_name != None:
            print("in student loop")
            for s in self.students:
                if s.name == student_name:
                    temp_student = s
                    print("student now temp")

        if course_name != None and course_section != None:
            
            print("in course loop")
            for c in self.courses:
                if c.course_name == course_name and c.section == course_section:
                    c.add_student(temp_student)
                    print("sutdent added")
                    return True

            return False


    def add_student_to_course_by_number(self,student_number:int,course_number:int, course_section:int):
        temp_student = None

        if student_number != None:
            for s in self.students:
                if s.student_number == student_number:
                    temp_student = s

        if course_number != None and course_section != None:
            for c in self.courses:
                if c.course_num == course_number and c.section == course_section:
                    c.add_student(temp_student)
                    print("added student")
                    return True

            return False

      
    
    def remove_student_from_course(self, student: Student, course: Course):
        temp_student = None

        if student != None:
            for s in self.students:
                if s.name == student.name:
                    temp_student = s

        if course != None:
            for c in self.courses:
                if c.course_num == course.number and c.section == course.section:
                    c.remove_student(temp_student)
                    print("removed course")
                    return True

            return False


    def remove_student_from_course_by_name(self,student_name:str,course_name:str, course_section:int):
        temp_student = None

        if student_name != None:
            for s in self.students:
                if s.name == student_name:
                    temp_student = s

        if course_name != None and course_section != None:
            for c in self.courses:
                if c.name == course_name and c.section == course_section:
                    c.remove_student(temp_student)
                    print("removed student from course by name")
                    return True

            return False


    def remove_student_from_course_by_number(self,student_number:int,course_number:int, course_section:int):
        temp_student = None

        if student_number != None:
            for s in self.students:
                if s.student_number == student_number:
                    temp_student = s

        if course_number != None and course_section != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    c.remove_student(temp_student)
                    print("removed student from course by num")
                    return True

            return False