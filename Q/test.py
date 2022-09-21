class Queue:
    def __init__(self,list1=[]):
        self.items=list1
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def dequeue(self):
        return self.items.pop(0)
    def enqueue(self,value):
        self.items.append(value)
    def top(self):
        return self.items[0]
Q=Queue()
print(Q.isEmpty())
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
print(Q.dequeue(),Q.dequeue(),Q.dequeue(),Q.top(),Q.isEmpty())
print(Q.items)