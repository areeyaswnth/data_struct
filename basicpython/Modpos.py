from typing import List


def mod_position(arr, s):
    ls=[]
    for n in range(0,len(arr)-2):
        if((n+1)%s==0):
         ls.append(arr[n])
    return ls

    
print("*** Mod Position ***")   
str1= input("Enter Input : ")
num=int(str1[-1])
print(mod_position(str1,num))