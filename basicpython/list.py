def odd_list(al):
    op=[]
    for n in range(len(al)):
        if(al[n]%2==1):
            op.append(al[n])
    return op
            
            
print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)

