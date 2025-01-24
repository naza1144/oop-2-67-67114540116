from student import Student
paul = Student("not", 4.0)
# print("pual.gpa:", Student.gpa)
print("Student.name=", paul.name)
print("Student.grade=", paul.grade)
print("Student.year=", paul.year)
paul.study_hard()
print(paul)
tony = Student("Tony", 3.99)
tony.year = 2
print(paul < tony)