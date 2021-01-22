# '''ls =[]
# for i in range(50):
#     if i%3==0:
#         ls.append(i)
#
# print(ls)'''
#
# ls= [i for i in range(50) if i%3==0]
# print(ls)
#
# dict1={i:f'item{i}' for i in range(1,20) if i%3==0}
# print(dict1)
#
# l=[i for i in range(0,10) ]
# l1=[value**3 for value in l]
# '''for value in l:
#     l1.append(value*value)
# '''
# print(l,l1)
#
# l2=[(value1,value2) for value1 in range(1,5) for value2 in range(100,103)]
# print(l2)
#
# a=[[1,2,3],[4,5,6],[7,8,9]]
# a1=[val2 for val1 in a for val2 in val1]
# #a2=[val3 for val3 in a1 if val3%3==0]
# a2=['Even' if val3%2==0 else 'Odd' for val3 in a1]
# '''
# for val1 in a:
#     for val2 in val1:
#         a1.append(val2)
# '''
# print(a1)
# print(a2)
#
#
# #1:1 2:2 ...
#
# d={x:x**2 for x in range(1,11)}
# print(d)
#
# #a:97 ,b:98,c='99....z:122
# d1={chr(x):x for x in range(97,123)}
# print(d1)
#
# d2={value:key for key,value in d1.items()}
# print(d2)
#
#


ls= [x for x in range(2, 500) if all(x % y != 0 for y in range(2, x))]
print(ls)