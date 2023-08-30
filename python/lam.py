def con(lst):
    lst = list(map(int,lst))
    print(lst)
    return lst
def a(ref):
    def b(lst):
        if 0 in lst:
            print(0)
        else:
            ref(lst)
    return b
@a
def M(lst):
    p = 1
    for i in lst:
        p *= i
    print(p)

lst = input('enter:').split()
lst = con(lst)
M(lst)