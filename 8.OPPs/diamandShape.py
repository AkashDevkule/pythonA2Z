class A:
    def printd(self):
        print("This is a method from class A.")
class B(A):
    def printd(self):
        print("This is a method from class B.")
class C(A):
    def printd(self):
        print("This is a method from class C.")
class D(C,B):
    pass




a=A()
b=B()
c=C()
d=D()

d.printd()
