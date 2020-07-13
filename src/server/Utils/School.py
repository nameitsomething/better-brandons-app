from Utils.Student import Student
import csv



class School:
    def __init__(self):
        self.students = []

    def add_student(self, name,age,grade,present):
        if present == "True":
            temp = True
        else:
            temp = False
        thing = Student(str(name),int(age),int(grade),temp)
        self.students.append(thing)

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
                     

    def find_info(self, name: str): #finds info
        for s in self.students:
            if s.name == name:
                return s

    def write(self): #writes the info in the list back into the file
        with open ('people.csv', "w", newline='') as file:
            writer = csv.writer(file,delimiter=',')

            for s in self.students: #think of the list as a container and s is for rows, so it writes out info in list
                writer.writerow(s.full_to_csv()) #writes onto file
                print(s)