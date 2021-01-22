# Sets:
# 1-mutable
# 2-unique element
# 3-immutable element
# 4-unorder

# s={10,2,2,2,40,5}
# print(s,type(s))

'''s={100,2,1231}
s.add(500)
print(s)
'''

s1={10,20,30,40}
s2={40,50,60}
'''s3=s1.union(s2)
print(s3)
'''
'''s3=s1.difference(s2)
print(s3)
'''
'''s3=s2.difference(s1)
print(s3)
'''
'''s3=s1.symmetric_difference(s2)
print(s3)
'''
'''print(s1)
s1.update(s2)
print(s1)'''


#print comman elemrnt btw'n s1 and s2
'''s1.intersection_update(s2)
print(s1)'''


'''s1.difference_update(s2)
print(s1)'''

'''s1.symmetric_difference_update(s2)
print(s1)'''

s4={100,200,300,400,500}
s5={100,200,300}

''' print(s5.issubset(s4))'''
'''l=[10,20,40]
s=set(l)
print(s)

l1=[10,10,20,23,22,22]
l2=[11,20,10,1,10]

s4=set(l1)
s5=set(l2)
print(s4,s5)
s6=s4.union(s5)
print(s6)

s6=list(s6)
print(s6)
'''




set1=set()
for i in range(10):
    set1.add(i)
print(set1)
print(type(set1))