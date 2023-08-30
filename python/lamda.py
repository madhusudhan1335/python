def add(num):
    return lambda x : x*num

n = int(input("enter number:\n"))
math_table = add(n)#stores in x
for i in range(1,11):
    print(n,"x",i,"=",math_table(i))