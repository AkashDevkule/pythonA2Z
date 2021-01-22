"""
Iterable- __iter__() or __getitem__()
Iterator- __next__()
Iteration-
"""
'''def gen(n):
    for i in range(n):
        yield i

g =gen(2)
'''# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
'''for i in g:
    print(i)

a='Akash'
ier=iter(a)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
'''
# for c in a:
#     print(c)


def fibo():
    a=0
    b=1
    yield b
    while(True):
        c=a+b
        yield c
        a,b=b,c


f=fibo()
# print(f)
#print(next(f))

for value in range(10):
    print(next(f))




print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

def printVal(L):
    for value in l:
        yield (value)



l=[10,20,30,40,50]
print(next(printVal(l)))

