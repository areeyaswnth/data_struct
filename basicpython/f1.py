import math
from pickletools import read_unicodestring1


class Spherical:

    def __init__(self, radius):

        self.radius = radius

    def changeR(self, Radius):
        self.radius = Radius

    def findVolume(self):
        return ( (self.radius**3) * 4 * math.pi) / 3

    def findArea(self):
        return math.pi*(self.radius**2)*4

    def __str__(self):
        str1 = "Radius ="+str(self.radius)+" Volumn = " +str(self.findVolume())+" Area = "+str(self.findArea())
        return str1


r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)
