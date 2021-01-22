d={
    'name':'Akash',
    'age':21,
    'city':'satara'
}

print(d)
print(d['name'])

'''          1.get         '''

print(d.get('agess','The is no key like age'))
print(d.setdefault('name'))
print(d)
print(d.setdefault('Roll',15))
print(d)


for key in d:
    print(key,d[key])


d1={}
for value in range(1,11):
    d1[value]=value*value
print(d1)

print(d.keys())
print(d.values())
print(d.items())

for i in d.values():
    print(i)

for j in d.items():
    print(j)

for i in d.keys():
    print(i)

#list
l1=[1,2,3]
l2=[21,15,5,4]

d=dict(zip(l1,l2))
print(d)

d=dict.fromkeys(l1,0)
print(d)

d1={1:1,2:4,3:9}
d2={4:16,5:25}
#merge Dict
d1.update(d2)
print(d1)

r=d1.pop(2)
print(d1,r)

r1=d1.popitem()
print(d1,r1)

d1.clear()
print(d1)


