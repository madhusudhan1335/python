add = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
div = lambda a,b : a/b
powe = lambda a,b : a**b
choice = input('enter your choice: ')
c = '+*-/"**"'
if choice in c:
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    if choice == '+':
        print(add(a, b))
    elif choice == '-':
        print(sub(a, b))
    elif choice == '*':
        print(mul(a, b))
    elif choice == '/':
        print(div(a, b))
    elif choice == '**':
        print(f'{powe(a, b):3e}')
else :
    print('Option is not present: Try again .........')
