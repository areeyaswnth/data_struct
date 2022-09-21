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


def printQ(q: Queue):
    Q2 = Queue([])
    if (q.isEmpty()):
        print("Empty", sep='', end='')
        return 0
    while (not (q.isEmpty())):
        n = q.deQueue()
        print(n, sep='', end='')
        if (q.size() >= 1):
            print(', ', sep='', end='')
        Q2.enQueue(n)
    while (not (Q2.isEmpty())):
        q.enQueue(Q2.deQueue())


Q1 = Queue([])
dQ = Queue([])

ls = [str(e) for e in input("Enter Input : ").split(",")]

for i in ls:
    if (i[0] == 'E'):
        Q1.enQueue(i.replace('E ', ''))

    if (i[0] == 'D'):
        if (not Q1.isEmpty()):
            n = Q1.deQueue()
            dQ.enQueue(n)
            print(n+' <- ', sep='', end='')
    printQ(Q1)
    print("")
printQ(dQ)
print(' : ', sep='', end='')
printQ(Q1)
