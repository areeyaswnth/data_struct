class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        for val in self.items[-1::-1]:
            if i[0] == val[0]:
                if self.items.index(val) == self.size() - 1:
                    break
                self.items.insert(self.items.index(val) + 1, i)
                return
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]


Q1 = Queue([])
Q2 = Queue([])

ls=[str(e) for e in input("Enter Input : ").split('/')]
Id=dict()
for i in ls[0].split(','):
    i = i.split()
    Id[i[1]] = i[0]

for i in ls[1].split(','):
    i = i.split()
    if i[0] == 'D':
        if Q1.isEmpty():
            print("Empty")
        else:
            print(int(Q1.deQueue()[1]))
    elif i[0] == 'E':
        i[0] = Id[i[1]]
        Q1.enQueue(i)