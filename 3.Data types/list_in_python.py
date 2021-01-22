'''# l=[]
# 1-mutable- can change
# 2-ordered - indexing and slicing
# 3-heterogeneous-any type of data stored
l=[10,20,30,40,'PYTHON','rADHE',[100,200,300]]
print(l,type(l))

# indexing and slicing
print(l[1])
print(l[-1])
print(l[-1][1])

#slicing
print(l[1:3])
print(l[::-1]) #reverse

for value in l[::2]:
    print(value)

#insert - append
a=[10,20,30,40]
print(a,id(a))   #same memory location
a.append(50) #added at the end
print(a,id(a))

# extend - multiple element insert
a.extend([60,70,80]) #added  at the end
print(a)
a.extend('Ram')
print(a)

# Insert-add at some position
a.insert(1,'Hare') #not add multiple element
print(a)

b=[10,20,30]
b1=b.copy()
b.append(40)
print(id(b),id(b1))
print(b,b1)


# pop,remove,clear,del
c=['Akash','Om','Shubham','Dada']


# print(c.pop(),c)
# c.remove('Akash')
# print(c)
#l.clear()
# del c
c.sort()
print(c)

c.reverse()
print(c)

c1=sorted(c)
print(c1)

print(c.index('Om'))
print(c.count('Om'))


'''
'''
#Adding into array
arrr=[]
while(True):
    n=input('Enter the value-')
    if len(arrr)<=9:
        arrr.append(n)
        print(arrr)
    else:
        print(arrr)
        break
        '''

'''l=[10,20,30,40,'PYTHON','rADHE',[100,900,300]]
print(l,type(l))

l[6].sort()

print(l[6])
print('This is max element-',max(l[6]))
n=input('Enter the number of n ')

l[6].append(n)

print(l)
'''

'''l=[]
l1=[x for x in range(1, 11)]
print(l1)


l2=[]
for i in range(11,21):
    l2.append(i)
print(l2)

l.append(l1)
l.append(l2)
print(l)

d1={}
for value in (l2):
    d1[value]=value*value
print(d1)'''


'''
# This is a rewrite of the average grade program we have done previously.
# In this program, we will learn about
# 1. modify lists
# 2. delete elements in list
# 3. clear lists
# 4. remove specific elements in list

import math

# create an empty grades list
grades = []

print(" enter your choices - ")
while (True):
    print("Enter your choice - ")
    print("- 'enter' grades")
    print("- 'delete' grades")
    print("- 'update' grades")
    print("- 'clear' grades")
    print("- calculate 'average'")
    print("- 'exit'")

    choice = input("- ")
    if choice == "exit":
        break

    if choice == "enter":
        print("Enter grades. type e to exit")
        while True:
            grade = input(" --> ")
            if grade == "e":
                break
            else:
                grade = float(grade)
                grades.append(grade)
        print("You have entered - ")
        print(grades)

    elif choice == "delete":
        if len(grades) == 0:
            # there are no grades yet.
            print(" No grades input yet. Please try to input grades")
        else:
            print("Enter index to delete. type e to exit")
            while True or len(grades) != 0:
                index = 0
                print("index - grade")
                for grade in grades:
                    print(index, "\t", grade)
                    index = index + 1

                grade = input("-->")
                if grade == "e":
                    break
                else:
                    if int(grade) < len(grades):
                        grades.pop(int(grade))

    elif choice == "update":
        if len(grades) == 0:
            # there are no grades yet.
            print(" No grades input yet. Please try to input grades")
        else:
            print("Enter index to update. type e to exit")
            while True or len(grades) != 0:
                index = 0
                print("index - grade")
                for grade in grades:
                    print(index, "\t", grade)
                    index = index + 1

                grade = input("-->")
                if grade == "e":
                    break
                else:
                    if int(grade) < len(grades):
                        print("Changing grade")
                        print("--------------")
                        print("index - grade")
                        print(int(grade), "\t", grades[int(grade)])
                        print("enter new grade")
                        new_grade = input("-->")
                        grades[int(grade)] = float(new_grade)

    elif choice == "clear":
        if len(grades) == 0:
            # there are no grades yet.
            print(" No grades input yet. Please try to input grades")
        else:
            grades.clear()
            print("cleared all grades")
            print("=================")

    elif choice == "average":
        average = math.fsum(grades) / len(grades)
        print("Average --> ", average)
        print("=================")

    else:
        print("Enter valid choice - Try again")
'''

'''
##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# In this program we will learn
# 1 - Dictionary Data Structure
# 2 - Functions

import random

q = {"The capital of India is New Delhi": True,
     "The capital of China is Shanghai" : False,
     "The capital of Australia is Canberra" : True,
     "The capital of Brazil is Rio de Janiera": False,
     "The capital of United States is New York" : False,
     "The capital of Russia is St. Petersburg" : False,
     "The capital of Singapore is Singapore" : True
    }

def str_to_bool (s ) :
    if s == "true" or s == "True" :
        return True
    elif s == "false" or s == "False" :
        return False


while ( True ) :
    question = random.choice( list(q.keys()))
    answer = input ( question + " - ")
    answer = str_to_bool ( answer)
    if answer == q.get(question) :
        print ( " correct ")
    else :
        print ( " incorrect ")'''

'''##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# Give 2 sentences, identify
# 1. common words between the sentences
# 2. unique words across the sentences
# 3. words in first sentence that are not present in the second.
# 4. unique words across the sentences excluding the common words.

# In this program, we will learn about
# 1. set intersection
# 2. set union
# 3. set difference
# 4. multiple operations on sets

s1 = input("First Sentence - ")
s2 = input("Second Sentence - ")

# split and store in lists
l1 = s1.split(" ")
l2 = s2.split(" ")

# set intersection
common_words = set(l1) & set(l2)

# set union
unique_words = set(l1) | set(l2)

# set difference
first_not_second = set(l1) - set(l2)

# combine sets
unique_exclude_common = ( set(l1) | set(l2) ) - (set(l1) & set(l2) )

print ( "First sentence is ",s1)
print ( "Second sentence is ",s2)

print ( "Common words are - ", common_words)
print ( "unique words are - ", unique_words)
print ( "unique words in first that are not there in the second sentence - ", first_not_second)
print ( "unique words across sentences, excluding common words - ", unique_exclude_common)'''
