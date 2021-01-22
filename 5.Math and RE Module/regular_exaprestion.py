import re

''' Meta 
. - any char
[a-zA-Z] - char class a or b or c .....or z A or B or ...Z
[0-9] -digit class 0 or 2 .... or 9

+ - atleast one [a-z]+
* -zero or more

^ -start of the string
$ - end of string

? -optional

[a-z]{2,4}'''


# def getstring(str1,str2=None):
#     str1=re.sub('[a-z0-9,()./;:" "]','',str1)
#     return str1
#
#
# # str1=input('Enter the string:-')
# # print(getstring(str1))
#
# print('<----check the panCard is valid or not----->')
#
# panId='ABCDE1234A'
# r=re.compile('^[A-Z]{5}[0-9]{4}[A-Z]$')
# l=re.findall(r,panId)
# print(l)
#
# print('<-----Check the contact number is valid or not ------>')
#
# mob_no='8698732656'
# # r=re.compile('^[8-9][0-9]{9}$')
# r=re.compile('(\+91\s)?[8-9][0-9]{9}')
# '''l=re.findall(r,mob_no)
# print(l)'''
# z=re.search(r,mob_no)
# if z:
#     print(z.group())
# else:
#     print('match not found')
#
# print('<---check Date of barth -->')
# #dd-mm--yyyy
# dob='27/07/1999'
# r=re.compile('^(?P<date>[0-9]{2})/(?P<month>[0-9]{2})/(?P<year>[0-9]{4})$')
# '''r=re.compile('^[0-9]{2}/[0-9]{2}/[0-9]{4}$')
# l=re.findall(r,dob)
# print(l)'''
#
# m=re.search(r,dob)
# if m:
#     print(m.group(2))
#     print(m.group('year'))
#     print(m.group('month'))
# else:
#     print('Not found Pattern')

'''def check_valid_mn(mn):
    r=re.compile('(\+91-)?^[8-9]{1}[0-9]{9}$')
    # l=re.findall(r,mn)
    # return l
    m=re.search(r,mn)
    if m:
        x=m.group()
        print(f'This {x} in valid numbar.')
    else:
        print (f'This {mn} number is not.')

n=input('Enter an 10 digit number-')
check_valid_mn(n)'''
class Name:
    def __init__(self,aname):
        self.name=aname


    def check_name(self,name):
        r=re.compile('^[A-Z]+[a-z]*')
        m=re.search(r,self.name)
        if m:
            x=m.group()
            print(x)
        else:
            print('Not valid',self.name)

    def d(self):
        print(self.name)

name=input('Enter the name you have to check-')
name1=Name(name)
name1.check_name(name1)
