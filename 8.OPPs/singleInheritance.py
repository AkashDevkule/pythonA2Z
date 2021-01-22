class Employee:
    def __init__(self,aname,aid):
        self.name=aname
        self.id=aid

    def printdetails(self):
        print(f"The employee '{self.name}' and id number is '{self.id}'.")

    @classmethod
    def printbystring(cls,string):
        return cls(*string.split('-'))

class Employeedetails(Employee):
    def __init__(self,aname,aid,alang):
        self.name=aname
        self.id=aid
        self.lang=alang

    def empdetails(self):
        print(f"The employee {self.name} knows {self.lang}\n")

emp1=Employee("Akash Devkule",'AG123')
emp2=Employee("Aniket Jadhav",12334)
emp3=Employee.printbystring("Shubham-SD2123")

emp4=Employeedetails("Omkar Khot",'SD3343',['Python','C++'])
emp4.printdetails()
emp4.empdetails()

emp1.printdetails()
emp2.printdetails()
emp3.printdetails()

