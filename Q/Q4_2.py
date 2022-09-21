class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

def insert(st1,st2):   
    t=[-1,-1]
    for i in range(Id.size()):
        n=Id.deQueue()
        if(st1 in n):
            st=n.replace(st1,'')
            t[0]=int((st.replace(' ','')))
        if(st2 in n):
            st=n.replace(st2,'')
            t[1]=int((st.replace(' ','')))
        Id.enQueue(n)  
    if(-1 not in t and t[0]==t[1]):
        c=1
    elif(-1 not in t and t[0]<t[1]):
        c=2  
    elif(-1 not in t and t[0]>t[1]):
        c=3
    else:
        c=0
    #print("st:",st1,st2,c,t[0],t[1])
    return  c

def check(str1,size):
    front=Queue()
    back=Queue()
    ins=insert(str1,Q2.peek())
    for num in range(size-2):
        if(ins==2):
            back.enQueue(Q2.deQueue())
        elif(ins==3):
            front.enQueue(Q2.deQueue())
        elif(ins==1):
            front.enQueue(Q2.deQueue())
        else:
            Q2.deQueue()
    while not front.isEmpty():
        Q2.enQueue(front.deQueue())
    if(ins!=0):
        Q2.enQueue(str1)
    while not back.isEmpty():
        Q2.enQueue(back.deQueue())
    print(Q2.items)



Q2 = Queue([])

ls=[str(e) for e in input("Enter Input : ").split('/')]
Id=Queue(ls[0].split(','))
Q1=Queue(ls[1].split(','))
while(not Q1.isEmpty()):
    st=Q1.deQueue()
    if(st[0]=='D'):
        if(Q2.isEmpty()):
            print("Empty")
        else:
            print(Q2.deQueue())
    else:
        if(Q2.isEmpty()):
            Q2.enQueue(st.replace('E ',''))
        else:
            check(st.replace('E ',''),Q2.size())    
    

   