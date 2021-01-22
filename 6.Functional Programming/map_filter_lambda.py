#map filter lambda

def sqr(num1):
    return num1**2

def check_num(num1):
    if num1%2==0:
        return True
    else:
        return False


l=[10,11,32,55,20,30]
result=list(map(sqr,l))
print('This is a list of squre of element of l-',result)

result1=list(filter(check_num,l))
print('This is an even list of number in l-',result1)


# for value in result:
#     print(value)

# addtion of element of two diff list based of index


def add(n,n1):
    return n+n1

l1=[10,20,30]
l2=[10,20,30]
result=list(map(add,l1,l2))
print(result)

result2=list(map(lambda n,n1:n+n1,l1,l2))
print('This is an list using lambda function-',result2)

#lambda
d={3:20,4:10,1:30,2:60}
l=sorted(d.items()) #sorted on key bases
print('sorted on key bases-',l)
l2=sorted(d.items(),key=lambda x:x[1])
print('This is should be on the value bases-',l2)