from Utils.School import School
from Utils.Student import Student
from Utils.Course import Course

school = School()

school.add_student(Student("bruh",222222229,858485,False))
print(school.find_student_info("bruh").student_number)

print(school.add_student(Student("Gabe", 12, 12, False)))
school.remove_student_by_number(2)
print(school.find_student_info(number=2))
