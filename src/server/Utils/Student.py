class Student:
    def __init__(self,name:str,age:int,grade:int,present:bool):
        self.name = name
        self.age = age
        self.grade = grade
        self.present = present
        self.student_number = 0

    def set_student_number(self, number: int):
        if number > 0:
            self.student_number = number
        

    def check_in(self):
        if not self.present:
            self.present = True

    def check_out(self):
        if self.present:
            self.present = False

    def full_to_csv(self):
        temp = []
        temp.append(self.name)
        temp.append(self.age)
        temp.append(self.grade)
        temp.append(self.present)
        temp.append(self.student_number)
        return temp

    def full_to_bytes(self):
        temp = f"{self.name},{self.age},{self.grade},{self.present},{self.student_number}"
        return str.encode(temp)
