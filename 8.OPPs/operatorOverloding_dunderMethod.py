class Employee:
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary

    def __add__(self, other):
        return f"{self.name+other.name}"

    def __truediv__(self, other):
        return self.salary /other.salary

    def __repr__(self):
        return f"Employee('{self.name}' ,{self.salary})"

    # def printd(self):
    #     return emp1.name

    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}."

emp1=Employee("Akash",2000)
emp2=Employee("Aniket",10000)

print(emp1 / emp2)
print(emp1 + emp2)
#print(emp2)


print(repr(emp1))
print(str(emp1))




