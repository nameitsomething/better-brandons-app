from server.Utils.Student import Student
from datetime import datetime

class Course:
    def __init__(self, course_name: str, description: str,section: int, course_num: int):
        self.course_name = course_name
        self.description = description
        self.section = section
        self.course_num = course_num
        self.students = []
        self.times = []
         
    def student_in_by_student (self, student:Student): # student checking in 
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    s.check_in() #calls check in function
                    return True

    def student_in_by_name(self, name: str):
        if name != None:
            for s in self.students:
                if s.name == name:
                    s.check_in()
                    return True
    def student_in_by_number(self, number):
        if number != None:
            for s in self.students:
                if s.student_number == number:
                    s.check_in()
                    return True


    def student_out_by_student (self, student:Student): # student checking in 
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    s.check_out() #calls check in function
                    return True


    def student_out_by_name (self, name):
        if name != None:
            for s in self.students:
                if s.name == name:
                    s.check_out()
                    return True

    def student_out_by_number(self, number):
        if number != None:
            for s in self.students:
                if s.student_number == number:
                    s.check_out()
                    return True


    def get_info(self):
        pass


    def who_is_present(self):
        temp = []
        
        for s in self.students:
            if s.present == True:
                temp.append(s)

    def who_isnt_present(self):
        temp = []

        for s in self.students:
            if s.present == False:
                temp.append(s)

    def remove_time(self,time: datetime ): #removes time for a course
        if time !=None:
            for t in self.times:
                if t == time:
                    self.times.remove(t)
                    return True


            return False

    def add_time(self, time: datetime): #adds time for a course
        if time != None:
            for t in self.times:
                if t == time:
                    self.times.remove(t)
                    return True

            return False


    def format_csv(self):
        str_time = ""
        for t in self.times:
            str_time += f"{t.timestamp()}"
            
        students = ""
        for s in self.students:
            students += f"{s.student_number}"

        out = f"{self.course_name},{self.course_num},{self.section},{self.description}"
        out += str_time
        out += students

        return out


    def format_bytes(self):
        return str.encode(self.format_csv())

    def add_student(self, student:Student):
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    return False

            self.students.append(student)
            return True


    def remove_student(self, student:Student):
        if student !=None:
            for s in self.students:
                if s.name == student.name:
                    self.students.remove(s)

    def remove_student_by_name(self,name):
        if name != None:
            for s in self.students:
                if s.name == name:
                    self.students.remove(s)

    def remove_student_by_number(self,number):

        if number != None:
            for s in self.students:
                if s.student_number == number:
                    self.students.remove(s) 

    def full_to_csv_course(self):
        temp = []
        temp.append(self.course_name)
        temp.append(self.description)
        temp.append(self.section)
        temp.append(self.course_num)
        temp.append(self.students)
        return temp

    def to_bytes(self):
        temp = f"{self.course_name}{self.description}{self.section}{self.course_num}{self.students}"
        return str.encode(temp)

        


    





        