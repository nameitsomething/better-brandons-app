class Student:
    def __init__(self,name:str,age:int,grade:int,present:bool):
        self.name = name
        self.age = age
        self.grade = grade
        self.present = present

    def check_in(self):
        self.present = True

    def check_out(self):
        self.present = False
