from Utils.School import School
from Utils.Student import Student
from Utils.Course import Course

name = "bruh"
info = ""
course = "death"

school = School()

school.read()

temp = Student("bruh",222222229,858485,False)

school.add_student(temp)


#school.write()

temp = Course("death","teaching people the 101 of killing","666")

school.add_course(temp)

print(school.find_course_info(course).description)

school.remove_student(name)

school.write()


# print(info.age)



# make a dummy thing to test out if the funtion form the students actually works for not....... 
# also testing out the course thing



















