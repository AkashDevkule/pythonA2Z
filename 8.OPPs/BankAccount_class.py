class Account:
    count=0

    @classmethod
    def incre_count(cls):
        cls.count +=1
        return cls.count

    def __init__(self,cust_id,cust_name,intial_bal=0):
        self.__id=cust_id
        self.__name=cust_name
        self.__balance=intial_bal
        Account.incre_count()

    def get_balance(self):
        return self.__balance
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def deposite(self,ammount):

        self.__balance=self.__balance +ammount
        return self.__balance

    def withdraw(self,ammount):
        if ammount > self.__balance:
            return 'insufficient balance'
        self.__balance -=ammount
        return self.__balance


customer1=Account('1','Akash')

'''print(customer1.id,customer1.name,customer1.balance)
print(customer1.get_balance())
print(customer1.deposite(5000))
print(customer1.withdraw(5000))
'''


customer2=Account('2','Shubham')
customer3=Account('3','Omkar')

customer1.deposite(2000)
customer2.deposite(100)
customer3.deposite(100)

l=[customer1,customer2,customer3]

for obj in l:
    if obj.get_balance() < 1000:
        print(f'{obj.get_id()} the customer id of name {obj.get_name()} and balance is {obj.get_balance()}.')

print(customer2._Account__id)
print(customer1.__dict__)
print(customer2.__dict__)
print(customer3.__dict__)

print(Account.incre_count())