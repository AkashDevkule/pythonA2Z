#inmutable
#ordered - indexing and slicing

s="radhe radhe welcome to the python tutorial."

print(id(s))  #Memory location

#indexing
print(s[:])
print(s[:4])    #start from 0 to end 4 i.e 4-1 index value
print(s[::2])   #skip the alternate char of strung
print(s[::-1])


for value in s[0:3]:
    print(value)

#formating
num1=10
num2=20
print("The value of num1 is {} and the value of num2 is {}.".format(num1,num2))
print("The value of num1 is {val1} and the value of num2 is {val2}.".format(val1=num1,val2=num2))


print(id(s))
s=s.capitalize() #first char is capital other are lower
print(s)
print(id(s))

#upper ,lower ,title
print(s.upper())    #upper convert the all string into  capital format
print(s.lower())    #convert the all string into the lower case
print(s.title())    #first latter of the word in the string should be Capital.

# isupper
# islower
# istitle
# iscapitalize

#split and join
s1='HTML CSS Python Python Python'
l=s1.split(' ')
print(l)

s2=('-').join(l)
print(s2)

#mapping string - with maketrans and tranlate

s3='abcdefghi'
s4='123456789'

s5='Hare Krishna Hare Ram'
table=str.maketrans(s3,s4)   #replace the a to 1 ...b to 2
result=s5.translate(table)
print(result)

#index
#find
#rfind function

print('Python' in s1)
print(s1.index('Python'))

print(s1.find('fdsfsd'))  #it will gives an -1 if string does not find
print(s1.rfind('Python'))  #it will starting with Right side and give index

#remove the wihte spaces both side - strip
x='------Radhe Radhe------'
x1=x.strip('-')
print(x1)
#remove the white spaces from left side
x2=x.lstrip('-')
print(x2)
#remove the white spaces from Right side
x3=x.rstrip('-')
print(x3)


#fix length

z='Krishna'
z1=z.center(20,'-')
print(z1)
z2=z.ljust(20,'*')
print(z2)
z3=z.rjust(20,'*')
print(z3)

y='html,pyhton,css,html'
y1=y.replace('html','html5')
print(y1)
