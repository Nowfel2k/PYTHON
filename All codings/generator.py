def gen(x, y):
    while(x<y):
        yield x
        x += 1
result = gen(20,30)
print(list(result))

'''List Comprehensions'''

lis = []
lis = [a for a in range(1,30, 2)]
print(lis)

p = [1,2,3,4,7,8,9]
q = [3,4,6]
r = [7,8,10]
s = []
s = [i for i in p if i in r]

print(s)




