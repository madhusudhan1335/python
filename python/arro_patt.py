try:
    num = int(input('enter:'))
except Exception as e:
    print(e)

x=num//2
for i in range(0,num):
    for j in range(0,num):
        if j>x:
            if j==x:
                continue
            print('*',end='')
        else:
            print(' ',end='')
    print()
    if i<num//2:
       x -= 1
    else:
       x += 1