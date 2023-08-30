def get_sum(lst):
    print(sum(lst))
def get_product(lst):
    p = 1
    for i in lst:
        p *= i
    print(i)
def fun(choice):
    if choice == 'sum':
        return get_sum
    else:
        return get_product
fun1 = fun('sum')
fun1([10,20,30,40])
fun2 = fun('product')
get_product([10,20,30,40])