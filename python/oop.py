class marks:
    def __init__(self,name,subject,marks):
        self.name = name
        self.subject = subject
        self.marks = marks
    def grade(self):
        if self.marks > 70 and self.marks < 80 :
            print('average')
        elif self.marks > 80 and self.marks < 90 :
            print('good')
        elif self.marks > 90 and self.marks < 100 :
            print('excelent')
    def display(self):
        print(self.name,end = '\t')
        print(self.subject,end = '\t')
        print(self.marks)

def main():
    result = marks('madhu','computers',95)
    result.display()
    result.grade()
    
    result1 = marks('sanju','computers',98)
    result1.display()
    result1.grade()

if __name__ == '__main__':
    main()