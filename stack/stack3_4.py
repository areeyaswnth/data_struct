



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

def check(st:Stack,i):
    if(st.isEmpty()or st.peek() != i):
        return True
    elif(st.size()>1):
        n = st.pop()
        if st.peek() == i:
            st.pop()
            return False
        else:
            st.push(n)
            return True
    else:
        return True
        



s=Stack(input('Enter Input : ').split())
temp=Stack([])
c=0


while(not s.isEmpty()) :
    if(check(temp,s.peek())):
        
        temp.push(s.pop())
        print(temp.items)
    else:
        print(s.pop())
        c+=1

print(temp.size())
while not temp.isEmpty():
    s.push(temp.pop())
if s.isEmpty():
    print("Empty",sep="",end="")
else:
    while( not s.isEmpty()):
        print(s.pop(),sep="",end="")
if c> 1:
    print("\nCombo : ",c," ! ! !",sep="",end="")
