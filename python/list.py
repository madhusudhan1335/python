lst = [10,20,30,40,50,60]
print(lst)
lst.append(70)#add element at end of list
print(lst)
lst.insert(3,35)#add element at any index, instert(index,value)
print(lst)
lst[4] = 80
print(lst)
lst.pop()#used to delete last element,when there is no index
print(lst)
lst.pop(2)#used to pop element at index value
print(lst)
lst.remove(20)#used to remove value in list
print(lst)
del lst[1]#used delete value at index or portion of list
print(lst)
del lst[0:2] #used to delete the portion of list
print(lst)