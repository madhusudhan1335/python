from abc import ABC, abstractmethod 
class Student(ABC):
    school = 'School = IBM'
    def __init__(self,name,age,gender,identity_num):
        self.name = name
        self.age = age
        self.gender = gender
        self.identity_num = identity_num
    @abstractmethod
    def std(self):
        pass
    @abstractmethod
    def Grades(self):
        pass
    @abstractmethod
    def evalution(self):
        pass
    def __str__(self):
        return f'name = {self.name}\nage = {self.age}\ngender = {self.gender}\nId_number = {self.identity_num}\n{self.school}'

class grade_A(Student):
    def std(self):
        print('standed  = 1st')
    def Grades(self):
        print('grade = A')
    def evalution(self):
        print('Good at study and Average at sports ')
   
class grade_B(Student):
    def std(self):
        print('standed  = 2st')
    def Grades(self):
        print('grade = B')
    def evalution(self):
        print('Average at study and Good at sports ')
   
class grade_C(Student):
    def std(self):
        print('standed  = 3st')
    def Grades(self):
        print('grade = A+')
    def evalution(self):
        print('Good at study and Good at sports ')

def display(ref):
    print('----Details-Students:---------')
    print(ref)
    ref.std()
    ref.Grades()
    ref.evalution()

std1 = grade_A('madhu',23,'M',1335)
std2 = grade_B('loner',23,'M',13)
std3 = grade_C('leo',22,'M',1131)

display(std1)
display(std2)
display(std3)

   