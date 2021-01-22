class enemy:
    hp=100
    def __init__(self,atkl,atkh):
        self.atkl=atkl
        self.atkh=atkh

    def getatk(self):
         print('The atklow is-',self.atkl)

    @classmethod
    def gethp(cls,newhp):
        cls.hp=newhp
        print(f"The new hp of  is {newhp} ")

    def gethp1(self):
        print("Hp of enemy is-",self.hp)

    @staticmethod
    def printwin(nameofenemy):
        print (nameofenemy + " is good player.\n"  )


if __name__ == '__main__':

    n=int(input('Enter the atkl value- '))
    m=int(input('Enter the atkh value- '))
    enemy1=enemy(n,m)
    enemy1.getatk()
#enemy1.gethp1()            return hp 100;
    enemy1.gethp(12)            #return hp 12
    enemy1.printwin("enemy1")

    enemy2=enemy(55,66)
    enemy2.getatk()
    enemy2.gethp1()
    enemy2.gethp(34)

    enemy2.printwin("enemy2")
