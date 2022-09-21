class funString(str):
    def __init__():
        str1=str

    def __str__():

        print('')

    def size() :
        return len(str)

    def changeSize():
        for n in range(0,len(str)):
            if(str[n]>='A' and str[n]<='Z'):
                str[n]+=32
            elif(str[n]>='a' and str[n]<='z'):
                str[n]-=32
        return str
    def reverse(self):
        strcp=[]
        for n in range(-len(str),0):
            strcp.append(len[n])
        return strcp

    def deleteSame(self):
        strch=[str[0]]
        for n in range(1,len(str)):
            for m in  range(0,len(strch)):
                if(str[n]!=strch[m]):
                    strch.append(str[n])
            



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())