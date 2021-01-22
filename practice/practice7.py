'''7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java'''

'''filename=input("Enter file name with . extension:-")
filename=filename.split('.')
print(filename[-1])
'''

str1=input('Enter the string-')


# print(len(str1))
# str1=str1.center(23,'*')
# print(str1)

# print(str1.capitalize())
# print(str1.isupper())
#print(str1.islower())

s1='kash'
s2='KASH'

l=str.maketrans(s1,s2)
r=str1.translate(l)
print(r)


l=str1.split(' ')
print(l)

for value in l:
    print('The value is {} the length of value is {} this is present at the this index-{}.'.format(value,len(value),l.index(value)))

l=('').join(l)
print(l)

