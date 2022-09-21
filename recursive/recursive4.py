
def SumSB(ls,index,S,B):
    global min
    if(index!=len(ls)):
        
        S=S*ls[index][0]
        B=B+ls[index][1]
        return SumSB(ls,index+1,S,B)
    else:
        return abs(S-B)
def findMin(ls):
    min=1000000000
    for i in combs(ls):
        if(len(i)>=1):
            S=1
            B=0
            temp=SumSB(i,0,S,B)
            if(temp<min):
                min=temp
    return min

        
def combs(a):
    S=1
    B=0
    if len(a) ==0 :
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs 
    
ls1 = [str(e) for e in input("Enter Input : ").split(',')]
ls2=[]
for i in ls1:
    ls2.append([int(e) for e in i.split(' ')])

print(findMin(ls2))
# for j in range(len(ls2)):
#     for
#      for

# print(SumSB(ls2,0))