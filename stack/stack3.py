
class Stack:
    def __init__(self, list1=[]):
        if list1 == None:
            self.items = []
        else:
            self.items = list1

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


S1 = Stack()

inp = input('Enter Input : ').split()

temp = ""
c=0
for i in inp:
    S1.push(i)
S2 = Stack([])
for i in range(len(inp)):
    if (S2.isEmpty()):
        print("1")
        S2.push(S1.pop())
    elif(not S2.isEmpty() and S1.peek()!=S2.peek()):
        if(S1.peek() not in temp):  
            print("2")
            S2.push(temp)
            S2.push(S1.pop())

    elif(not S2.isEmpty() and  S1.peek()==S2.peek()):
        if(S1.peek() not in temp):        
            print("4")
            temp+=S1.pop()
        elif(S1.peek()in temp ):
            temp.replace(S1.peek(),'')  
            S2.pop()
            S1.pop()
            print("5")
            c+=1



  
print(temp)
### Enter Your Code Here ###
print(S2.size())
size=S2.size()
for i in range(S2.size()) :
    S1.push(S2.pop())
for i in range(S1.size()) :
    print(S1.pop(),sep="",end="")
if(c>1):
    print("\nCombo : ",c," ! ! !",sep="",end="")
if(size==0):
    print("Empty")

### Enter Your Code Here ###
