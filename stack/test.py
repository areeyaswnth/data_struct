class Stack:
    def __init__(self,list1=[]) :
        self.items=list1
    def isEmpty(self):
        return self.items==[]
    def push(self,value):
        self.items.append(value)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
st=Stack()

print(st.isEmpty())
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.pop()
st.pop()
print(st.peek())
print(st.isEmpty())
print(st.size())
print(st.items)