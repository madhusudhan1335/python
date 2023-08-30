class Lis(list):
    def display(self):
        for i in self:
            print(i)

class Arr:
    li = Lis()
    print('hi')
    def __init__(self,name):
        self.name = name
        Arr.li.append(self)
    def dis(self):
        print('in array')
    
a = Arr('mad')
b = Arr('hello')
c = Arr('cat')
#Arr.li.display()
