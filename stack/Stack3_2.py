
from inspect import stack


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

combo = 0
s = Stack(input('Enter Input : ').split())
t = Stack()

def check(st: Stack, i):
    if st.isEmpty() or st.peek() != i:
        return True
    if st.size() > 1:
        x = st.pop()
        if st.peek() == i:
            st.pop()
            return False
        else:
            st.push(x)
            return True
    else:
        return True

while not s.isEmpty():
    i = s.pop()
    if check(t, i):
        t.push(i)
    else:
        combo += 1
print(t.size())
if t.isEmpty():
    print("Empty")
else:
    print(*t.items, sep='')
if combo > 1:
    print(f"Combo : {combo} ! ! !")