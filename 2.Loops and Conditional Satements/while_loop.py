'''run=True
current=1
#print 1 to 100 numbrs
while run:
    if current==101:
        run=False
    else:
        print(current)
        current +=1'''

'''def fib(n):
    #result=[]
    a,b=0,1
    while a<n:
        print(a,end=' ')
        #result.append(a)
        a,b=b,a+b

    #return result
fib(2000)'''


'''lis1=[12,63,55]
print(type(lis1))
print(lis1.pop(1))
lis1.append(2)
print(lis1)
t1=tuple(lis1)
print(t1)
l1=list(t1)
print(l1)'''


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def factTrillingZeros(n):
    pass



if __name__ == '__main__':
    n=int(input("Enter the number:-"))
    fact=factorial(n)
    print(f'Factorial of {n} is {fact}')


