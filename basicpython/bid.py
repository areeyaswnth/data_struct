from tabnanny import check


x = list(map(int, input("Enter All Bid : ").split()))
max1= x[0]
max2=0
check=0;
x.sort()
if(len(x)>1):
    if(x[-1]>x[-2]) :
        print('winner bid is',x[-1],'need to pay',x[-2])
    elif(x[-1]==x[-2]):
        print('error : have more than one highest bid')
else:
    print('not enough bidder')
