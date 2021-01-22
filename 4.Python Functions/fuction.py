def my_function():
    print("This is my functon")
    print("This is Python"+'\n')

#fuction calling
my_function()


#passing argument to function
def my_function2(str1,str2):
    print(str1)
    print(str2)

my_function2("This is second function",'This is my string.\n')

#default arguments
def my_function3(name="Ram",age=22):
    print('My name is',name,'and my age is',age,'\n')

my_function3("Akash")

#keyword argument
my_function3(age=33)


#infinite argument
def my_frd(*friends):
    for friend in friends:
        print('This is my friend',friend,)

my_frd('omkar','Shubzz','Shubham')

#return value from the function

def do_math(num1,num2):
    return num1+num2

math1=do_math(10,5)
math2=do_math(21,5)
print('\nThe first sum is',math1,'and second sum is ',math2,'.')