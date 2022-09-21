
len=int(0)
st=""
def length(txt): 
    global len    
    if(txt==''):
        return len
        
    else:
        if(len%2==0):
            print(txt[0],'*',sep='',end='')
        else:
            print(txt[0],'~',sep='',end='')
        len+=1
        return length(txt[1:])
     #Code Here
print("\n",length(input("Enter Input : ")),sep="")
