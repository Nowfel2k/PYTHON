list1 = [2,4,456,31,77,98,23,11,234,24,34]

#Filter Function
result = filter(lambda x:x%2==0, list1)
print(list(result))

#Mapping Function
result2 = map(lambda n:n*2, list1)
print(list(result2))

#Reduce Function
from functools import reduce
list2 = [32,43,56,67,88]
result3 = reduce(lambda x,y:x+y, list2)
print(result3)

#Decorator Function
def decorator(fun):
    call = fun()
    return call**2
@decorator
def num():
    return 5
print(num)


