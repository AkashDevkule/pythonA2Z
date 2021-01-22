class Employee:
    def __init__(self,aname,aid):
        self.name=aname
        self.id=aid


    def printdetails(self):
        print(f"The employee {self.name}.")

class player():

    def __init__(self,aname,aid,agame):
        self.name=aname
        self.id=aid
        self.game=agame

    def playerdetails(self):
        print(f"The employee {self.name} knows {self.game}. ")


class proemployee(player,Employee):
    lang=['python','C++']
    def printlang(self):
        print(f"The languages {self.lang} ,knows {self.name}.")

emp1=Employee('Akash Devkule',123)
emp1.printdetails()


emp2=proemployee("Akash Devkule",123,'cricket')
emp2.printlang()
emp2.playerdetails()
