class Student(object):
    Student_count = 0 
    
    # def __new__(cls):
    #     print('Student.__new__')
    #     cls.gpa = 4.00

    def __init__(self, name = 'Anna', grade = 4.0):
        print('Student.__init__')
        self.name = name
        self.grade = grade
        self.year = 1

    def __repr__(self):
        return f'{self.name} is in year {self.year} grade {self.grade}'
    
    def __lt__(self, other):
        return self.year < other.year


    def study_hard(self):
        print('Sir, yes sir.')