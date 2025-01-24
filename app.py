class Student(object):
    Student_count = 0 
    
    def __new__(self):
        print('Student.__new__')

    def __init__(self):
        print('Student.__init__')
        self.gpa = 4.00

    def student_hard(self):
        print('Sir, yes sir.')

print(Student.__dict__)