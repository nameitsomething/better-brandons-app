from Utils.Student import Student
from Utils.Course import Course
import csv


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student): # adds student into student list
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    return False
      
            self.students.append(student)
            return True
 

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

    def check_in_student(self, student:Student = None, name: str = None, number: int = None): #master attendence
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    s.check_in()

        elif name !=None:
            for s in self.students:
                if s.name == name:
                    s.check_in()

        elif number !=None:
            for s in self.students:
                if s.student_number == number:
                    s.check_in()


    def write(self): #writes the info in the list back into the file
        with open ('people.csv', "w", newline='') as file:
            writer = csv.writer(file,delimiter=',')

            for s in self.students: #think of the list as a container and s is for rows, so it writes out info in list
                writer.writerow(s.full_to_csv()) #writes onto file

    def remove_student(self, student: Student, name :str =None, number: int = None): # yeets student into space
        if student != None: 
            for s in self.students:
                if s.name == student.name:
                    self.students.remove(s)
                    break

        elif name != None:
            for s in self.students:
                if s.name == name:
                    self.students.remove(s)

        elif number != None:
            for s in self.students:
                if s.student_number == number:
                    self.students.remove(s)
    
    def who_is_present(self):
        temp = []



    def add_course(self, course): # adds course 
        self.courses.append(course)
        pass

    def remove_course(self,course: Course = None,course_name:str = None, course_number:int = None ): # yeets course into space
        for c in self.courses:
            if c.course_name == course.name:
                self.courses.remove(c)
                break

    def add_time(self):
        pass

    def remove_time(self):
        pass

    def add_student_to_course(self, student: Student = None, student_name: str = None, student_number: int = None, course: Course = None, course_name:str = None, course_number:int = None, course_section:int = None):
        temp_student = None

        if student != None:
            for s in self.students:
                if s.name == student.name:
                    temp_student = s

        elif student_name != None:
            for s in self.students:
                if s.name == student.name:
                    temp_student = s

        elif student_number != None:
            for s in self.students:
                if s.student_number == student_number:
                    temp_student = s

        if temp_student == None:
            return False

        if course != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    c.add_student(temp_student)
                    return True

            return False

        elif course_number != None and course_section != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    c.add_student(temp_student)
                    return True

            return False

        elif course_name != None and course_section != None:
            for c in self.courses:
                if c.name == course_name and c.section == course_section:
                    c.add_student(temp_student)

    
    def remove_student_from_course(self, student: Student = None, student_name: str = None, student_number: int = None, course: Course = None, course_name:str = None, course_number:int = None, course_section:int = None):
        temp_student = None

        if student != None:
            for s in self.students:
                if s.name == student.name:
                    temp_student = s

        elif student_name != None:
            for s in self.students:
                if s.name == student.name:
                    temp_student = s

        elif student_number != None:
            for s in self.students:
                if s.student_number == student_number:
                    temp_student = s

        if temp_student == None:
            return False

        if course != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    c.remove_student(temp_student)
                    return True

            return False

        elif course_number != None and course_section != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    c.remove_student(temp_student)
                    return True

            return False

        elif course_name != None and course_section != None:
            for c in self.courses:
                if c.name == course_name and c.section == course_section:
                    c.remove_student(temp_student)





