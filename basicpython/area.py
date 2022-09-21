class funString():

    def __init__(self,string = ""):
        self.string=string
        

    def __str__(self):
        print("")
        ### Enter Your Code Here ###

    def size(self) :

        return len(self.string)

    def changeSize(self):
        strc=""
        for i in range(len(self.string)):
            if(self.string[i]>='A' and self.string[i]<='Z'):
                strc+=(chr(ord(self.string[i])+32))    
            elif(self.string[i]>='a' and self.string[i]<='z'):
                strc+=(chr(ord(self.string[i])-32))
        return strc

    def reverse(self):

         return self.string[::-1]

    def deleteSame(self):
        strc=""
        for i in range(len(self.string)):
            if(self.string[i] not in strc):
                strc+=self.string[i]

        return strc



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())