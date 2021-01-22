#from  abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod

'''class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=6

    def printArea(self):
        return f"Area={self.length * self.breadth}"



rect1=Rectangle()
print(rect1.printArea())

tryobj=Shape() #we can not create object like this.'''

class devkule(ABC):
    @abstractmethod
    def familymember(self):
        return 0

class Family(devkule):

    def __init__(self,lastname):
        self.lname=lastname

    def familymember(self):
        if self.lname=='Devkule' or self.lname=='devkule':
            return f'You are the member of {self.lname} Family.'
        else:
            return self.lname
mem1=Family('Sharma')

print(mem1.familymember())