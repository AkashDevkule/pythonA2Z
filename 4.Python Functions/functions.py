#builting fun'n
s="Python,HTML,CSS"
print(s.index('HTML'))

def reverse(value):
    if type(value)==list or type(value)==str:
        reverse=value[::-1]
        print(reverse)
    else:
        temp=str(value)
        reverse=temp[::-1]
        print(reverse)

def from_comma(str):
    str=str.split(',')

    print(str)


s="Python,HTML,CSS"
reverse(s)
from_comma(s)

l=[10,20,30]
reverse(l)

num=100
reverse(num)

print('----- defaul value keyword argument--------')
print(ord('A'),ord('Z'))
print(ord('a'),ord('z'))

print(chr(65))

import random

def get_pass(Lenght=8):
    l=['@','#','$','&']
    upper=chr(random.randint(65,90))
    lower=chr(random.randint(97,122))
    special=random.choice(l)
    digit=random.randint(10000,99999)
    password=upper + lower + special + str(digit)
    l = random.sample(password,Lenght)
    password = ("").join(l)
    if len(password)>=5:
        return f'Your password is {password} and it is Strong.'
    else:
        return f'{password} is too weak.'


result=get_pass()
print(result)

# variable length
print('********** verialble length argument **********')
def add_value(*args):
    l=[]
    for value in args:
        l.append(value)

    return l


result=add_value(10,2,2,33)
print(result)

result=add_value(100000000,2,2,33)
print(result)

print('-----variable lenght keyword argument-----')

#name,roll,email,dob
def get_details(**kwargs):

    print(kwargs)

get_details(name='abc',email='abc@gmail.com',dob='12-05-1999')
get_details(name='abc',dob='12-05-1999')
get_details(email='abc@gmail.com',dob='12-05-1999')

print('------- recurcive function-------')
print('------- recurcive function-Factorial ------')

def factorial(num1):
    if num1==1:
        return 1
    else:
        fact=num1*factorial(num1-1)
        return fact
num1=5
result=factorial(num1)
print(result)

print('-----binary_Search----')

def binary_serach(l,key):
    if len(l)==0:
        return False
    else:

        mid=len(l)//2
        if l[mid]==key:
            return True
        elif key<l[mid]:
            return binary_serach(l[:mid],key)
        else:
            return binary_serach(l[mid+1:],key)

if __name__ == '__main__':
    l=[100,200,300,400,500,600,700,800,900]
    key=500
    result=binary_serach(l,key)
    print(result)