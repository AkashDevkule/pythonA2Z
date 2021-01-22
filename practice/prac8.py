'''8. Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]'''

#color_list = ["Red","Green","White" ,"Black"]
#print(color_list[0],color_list[-1])

'''9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014'''

#exam_st_date ='(11, 12, 2014)'
#exam_st_date=exam_st_date.replace(',','/')
#print('The examination will start in from:-',exam_st_date.replace(',','/'))

'''10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615'''

#a = int(input("Input an integer : "))
#n1 = int( "%s" % a )
#n2 = int( "%s%s" % (a,a) )
#n3 = int( "%s%s%s" % (a,a,a) )
#print (n1+n2+n3)

#print(abs(121.2154))

'''12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.'''

'''import calendar
y=int(input("Enter the year:-"))
m=int(input("Enter the month:-"))
print(calendar.month(y,m))'''

''' 14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''
#from datetime import date

#f_date=date(2014, 7, 2)
#l_date=date(2014, 7, 11)
#delta=l_date-f_date
#print(delta.days)

'''16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.'''
#def getDiff(n):
#    if n<=17:
#        print(17-n)
#    else:
#        print(2*(n-17))
#n=int(input("Enter the number "))
#getDiff(n)

'''18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum'''

'''def sumDiff(n1,n2,n3):
    if n1==n2 and n2==n3 and n1==n3:
        return (3*(n1+n2+n3))
    else:
        return (n1+n2+n3)
print(sumDiff(10,12,13))
print(sumDiff(10,10,10))'''

'''19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.'''

'''def is_in_str(str1):
    if len(str1)>=2 and str1[:2]=="Is":
        return str1
    else:
        return ( str1.replace(str1[:2],'Is '))

print(is_in_str('I am Akash?'))
print(is_in_str('Is he akash?'))'''

'''22. Write a Python program to count the number 4 in a given list'''
#num=[5]
#print(num.count(4))

'''def count_num(nums):
    count=0
    for num in nums:
        if num==4:
            count +=1
    return count
print(count_num([4,5,4,3])'''

'''38. Write a Python program to solve (x + y) * (x + y). Go to the editor
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49

x,y=4,3
result=x*x+2*x*y+y*y
print(f'({x} + {y} ^ 2) = {result}')'''
'''
color1=set(['cc','bb'])
color2=set(['bb','cc'])

print(color1.difference(color2))'''

'''import os.path
open('ac.txt','w')
print(os.path.isfile('ac.txt'))'''

'''color1=['cc','bb']
color='-'.join(color1)
allcol='-'
print(color)
'''
'''x=20
y=30

print(f'"{x}+{y}={20+30}"')'''


'''def fib(n):
    #result=[]
    a,b=0,1
    while a<n:
        print(a,end=' ')
        #result.append(a)
        a,b=b,a+b
        
    #return result
fib(2000)
'''
#for i in range(5,10,2):
#    print(i)

'''def square(x):
    return x*x


def main():
    for i in range(11):
        print(r"{} square is {}".format(i,square(i)))


if __name__ == '__main__':
    main()'''


'''import re
str1=read()
print(f"hello {str1[1]}")
print(str1.replace('a','A'))
print(str1.isdigit())
print(re.sub('[a-z0-9,()./;:" "]','',str1))
print(str1.upper())'''




#Sum of container

''' s=sum([40,3,5])
 print('sum of conatiner is ',s)
'''

#Getting Size of  file
'''import  os
fileSize=os.path.getsize("prac8.py")
print("The size of fileIS-",fileSize)
'''

#sorting number without the conditional or loop statement
'''
a,b,c=10,22,9

a1=min(a,b,c)
a3=max(a,b,c)
a2=(a+b+c) - a1-a3
print(a1,a2,a3)'''

'''import os
print("The path of file is:-",os.path.realpath(__file__))
'''

# d1={}
# for value in range(1,11):
#     d1[value]=value*value
# print(d1)

name_dict={}

while(True):
    count = input('Enter \'e\' to exit or press Enter to continue"\n')
    if count != 'e':
        name = input('Enter name of item -> ').isalpha()
        name_dict[name] = int(input('Enter price  value of item -> ').isnumeric())
        # count+=1
    else:

        print(f'Your list of shopping items with there prices - {name_dict}')
        print(f'Your total shopping bill is- {sum(name_dict.values())}')
        print('Visit Again....Thank You!')
        break
