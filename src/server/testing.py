from Utils.School import School
from Utils.Student import Student
from Utils.Course import Course

school = School()

#school.add_student(Student("bruh",222222229,858485,False))

temp = Course("death","time to die",1,666)

school.add_course(temp)

school.read()

print(school.find_student_info("bruh").student_number)



print(school.add_student(Student("Gabe", 12, 12, False)))

print(school.students)

print(school.courses)

school.write()

print(school.find_student_info(number=2))
