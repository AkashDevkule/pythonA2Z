# class Dad:
#     cricket=1
#
# class Son(Dad):
#     Dance=2
#     cricket = 4
#     def isdance(self):
#         return f"Yess He dance very nicely {self.Dance} times in college ."
#
# class grandSon(Son):
#     Dan = 6
#     # def isdance(self):
#     #     return f"freeStyler he dance" \
#     #            f"Yeah he dance awesomely {self.Dance} number of times in college."
#
#
#
# darry=Dad()
# larry=Son()
# garry=grandSon()
#
# #print(larry.isdance())
# #print(garry.isdance())
#
# #print(larry.cricket)
# print(garry.cricket)

class electornic_devices:
    requried_power=100
    longlife=20

class pocket_device(electornic_devices):
    #requried_power = 50
    longlife=4
    def pddetails(self):
        return f"pocket device required less power than {self.requried_power}watt." \
               f"pocket device like watch."

class phone(pocket_device):
    requried_power = 20
    def pdetails(self):
        return f'phones reqired {self.requried_power} power.' \
               f'They have more {self.longlife} years lifetime.'

computer=electornic_devices()
watch=pocket_device()
mobile=phone()


# print(mobile.longlife)
# print(watch.longlife)


print(mobile.pdetails())
print(mobile.longlife)
print(watch.pddetails())