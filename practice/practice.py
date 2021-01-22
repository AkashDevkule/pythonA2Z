'''name=input()

print(name[1:])
print(name[:-1])
print(name[::-1])
print(name.upper())
print(name.lower())
'''
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

'''1)Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''
'''
item=input("\nEnter comma separeted value:-")
list=item.split(',')
tuple=tuple(list)
print('List:',list)
print('Tuple',tuple)
'''
'''
t=(10,1,334,55)
print(t)
print(t[0])
print(t[-1])
print(t.count(1))
print(t.index(55))

l=[10,25,56]
for t in enumerate(l):
    print(t)'''



