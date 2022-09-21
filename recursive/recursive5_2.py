
#บวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย


def asteroid_collision(index,asts:list):
    if(index+1 == len(asts)):
        return asts
    if(index+1<len(asts)):
        st1=int(asts[index])
        
        st2=int(asts[index+1])
        # print(st1,st2,index)
        if st1>0 and st2<0:
            if st1>abs(st2):
                asts.pop(index+1)
            elif st1<abs(st2):
                asts.pop(index)
            else:
                asts.pop(index+1)
                asts.pop(index)
            return asteroid_collision(index-1,asts)
        else:
            return asteroid_collision(index+1,asts)
            
    #Code Here

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(0,x))