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
class Stack:
    def __init__(self, list=[]):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

def check(st: Stack, i):
    if (st.isEmpty() or st.peek() != i):
        return True
    elif (st.size() > 1):
        n = st.pop()
        if st.peek() == i:
            st.pop()
            return False
        else:
            st.push(n)
            return True
    else:
        return True

inp = input('Enter Input (Normal, Mirror) : ').split(' ')
Qnormal = Queue()
Smirror = Stack()
temp = Stack([])
temp2 =Queue([])
st = Stack([])
c = 0

#mirror
for i in range(len(inp[0])):
    Qnormal.enQueue(inp[0][i])
for i in range(len(inp[1])):
    Smirror.push(inp[1][i])

while (not Smirror.isEmpty()):
    if (check(temp, Smirror.peek())):
        temp.push(Smirror.pop())
    else:
        temp2.enQueue(Smirror.pop())
        c += 1
while not temp.isEmpty():
     Smirror.push(temp.pop())
while not Smirror.isEmpty():
     st.push(Smirror.pop())

c2=0
F=0
while (not Qnormal.isEmpty()):
    if (check(temp, Qnormal.peek())):
        temp.push(Qnormal.deQueue())
    else:
         if(not temp2.isEmpty()): 
            n=Qnormal.deQueue()
            if(temp2.peek()!=n):
                temp.push(n)
                temp.push(n)
                temp.push(temp2.deQueue())
                temp.push(n)
            else:
                temp.push(temp2.deQueue())
                F+=1
                
         else:
            c2 += 1
            Qnormal.deQueue()

print("NORMAL :")
print(temp.size())
if(temp.isEmpty()):
    print("Empty", sep="", end="")
while (not temp.isEmpty()):
    print(temp.pop(), sep="", end="")
print()

print(c2," Explosive(s) ! ! ! (NORMAL)",  sep="")
if(F!=0):
    print("Failed Interrupted",F,"Bomb(s)")
print("------------MIRROR------------\n: RORRIM")
print(st.size())
if(st.isEmpty()):
    print("ytpmE", sep="", end="")
while (not st.isEmpty()):
    print(st.pop(), sep="", end="")
print()
print("(RORRIM) ! ! ! (s)evisolpxE ", c, sep="")

