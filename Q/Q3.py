






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

def check(q:Queue,i,size):
    q=Queue()
    for x in range(size):
        n=Q1.deQueue()
  
        if(int(i)==int(n)):
            q.enQueue(n)
        else:
            Q1.enQueue(n)
    if(q.isEmpty()):
        return False
    else:
        return True
  
        

       
        


Q1 = Queue([])
Q2 = Queue([])
d=0

ls=[str(e) for e in input("Enter Input : ").split('/')]

Q1=Queue(ls[0].split(' '))
Q2=Queue(ls[1].split(','))
while(not Q2.isEmpty()):
    n=Q2.deQueue()
    if(n[0]=='E'):
        Q1.enQueue(n.replace('E',''))
    else:
        Q1.deQueue()
#print(Q1.items)
while(not Q1.isEmpty()):
    if check(Q1,Q1.deQueue(),Q1.size()):
        d+=1
        #print(d)
if(d!=0):
    print("Duplicate")
else:
    print("NO Duplicate")