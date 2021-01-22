class A:
    branch="Civil"
    roll=10
    def __init__(self):
        #self.branch='Computer'
        #self.roll=15
        self.real="Computer is my real branch and roll is 15"
class B(A):
    branch="ENTC"
    def __init__(self):
        super().__init__()
        #self.branch='electrical'
        self.roll=50

class C(B,A):
    branch='IT'
    def __init__(self):
        super().__init__()
        self.branch='Mech'
        #self.roll=27

a=A()
b=B()
c=C()

print(c.branch,c.roll)
print(c.real)
