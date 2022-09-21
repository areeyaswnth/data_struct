def countdown(n):
    if(n<len(listt)):

        if(listt[n+1]==listt[n]-1 and n < len(listt)):
            list1.append(listt[n])
            return countdown(n+1)
        elif(listt[n]==1 and len(list1)>0):
            list1.append(listt[n])
            list2.append(list1) 
            return n+1
        elif(listt[n+1]!=listt[n]-1):
            #list1.clear()
            return n+1
list1=[]
list2=[]
print(" Fun with countdown ")
print("Enter List : ", end = '')
listt = [int(n) for n in input().split()]
for i in range(0,len(listt)-1):
    i=countdown(i)
    list1=[]
    #print(i)
print(list2)