class Student:
    
    def __init__(self,name,cla_ss,id_no):
         self.name = name 
         self.cla_ss = cla_ss
         self.id_no = id_no
        
    def display(self):
        print( self.name)
        print( self.cla_ss)
        print(self.id_no)
        
def main():
    std = Student('leo',10,1335)
    std.display()
         
if __name__=='__main__':
    main()