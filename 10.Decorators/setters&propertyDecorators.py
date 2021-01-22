class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{self.fname}.{self.lname}@vpkbiet.org"

    def printd(self):
        return f"The name is {self.fname} {self.lname}."

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set please set the email by setter."
        return f"{self.fname}.{self.lname}@vpkbiet.org"

    #syntax    if we wont to set email
    #    @email.setter
    @email.setter
    def email(self,string):
        print("Setting now...")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

     #for delete the setter
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


emp1=Employee("Akash","Devkule")
emp2=Employee("Aniket","Jadhav")

print(emp1.email)

emp1.fname="Shubham"
print(emp1.email)

emp1.email="thsajh.dfjkls@jjjas.vj" #for this we use an the setter decorator
print(emp1.email)

del emp1.email #delete
print(emp1.email)