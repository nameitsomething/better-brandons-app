from Utils.Student import Student
import csv



class School:
    def __init__(self):
        self.students = []

    def read(self): #reads the file and puts it into the list
        with open ('people.csv',"r", newline=' ') as file:
            reader = csv.reader(file, delimiter=',')

            for row in reader: 
                thing = Student(row[0],row[1],row[2],row[3]) #uses the student class to seperate the stuff
                self.students.append(thing) #appends stuff to the list
                print(thing)     

    def find_info(self, name: str):
        for s in self.students:
            if s.name is name:
                return s

    def write(self): #writes the info in the list back into the file
        with open ('people.csv', "w", newline='') as file:
            writer = csv.writer(file,delimiter=',')

            for s in self.students: #think of the list as a container and s is for rows, so it writes out info in list
                writer.writerow(s) #writes onto file
                print(s)