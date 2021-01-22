import itertools

l1=[10,20,30]
l2=[40,50,60]
l3=[70,80,90,100]

i=itertools.chain(l1,l2,l3)
print(i)
for value in i:
    print(value)
print('Here is end of chain.')

i=itertools.cycle(l1) #one by one element will cycle 9  times.
count=0
for value in i:
    if count < 9:
        print(value)
    else:
        break
    count+=1
print('End cycle')

i=itertools.repeat(l1)
print(next(i))
print(next(i))
print(next(i))


i=itertools.tee(l1,3)
for value in i[1]:
    print(value)

# for value in i[1]:
#     print(value)
print('The printing the tee function to itorate')

j=itertools.chain(l1,l2,l3)

for value in itertools.islice(j,0,5):
    print(value)

print('islice function start from 0 to end at 5')

count=0
for value in itertools.count(10,5):
    if count >20:
        break
    else:
        print(value)
    count+=1

print('it will print an start from 10 to inncremented by 5')

x1=[1,2,3,4,5]
print(list(itertools.permutations(x1,2)))
print('It will show all combination 1 to 6')
print(list(itertools.combinations(x1,2)))
print('combition of two numbers')

