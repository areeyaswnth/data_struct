


def asteroid_collision(asts,pos):
    if(pos<=0):
        return asts
    else:
        star1=asts[pos-1]
        star2=asts[pos]
        if(star1>0 and star2<0):
            if(abs(star1)>abs(star2)):
                asts.pop(pos)
            elif(abs(star1)==abs(star2)):
                asts.pop(pos)
                asts.pop(pos-1)
                pos=pos-1
            else:
                asts.pop(pos-1)
        return asteroid_collision(asts,pos-1)
        
    
    #Code Here

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x,len(x)-1))