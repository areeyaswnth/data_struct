

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


Q1 = Queue([])
Q2 = Queue([])
ls = [str(e) for e in input("Enter Input : ").split(sep=",",end="/")]
for i in ls:
    if ( 'EN' in i):       

        Q1.enQueue(i.replace('EN ', ''))
    elif (i[0] == 'D'):        
        while(not Q1.isEmpty()):
            Q2.enQueue(Q1.deQueue())
        while(not Q2.isEmpty()):
            Q1.enQueue(Q2.deQueue())
        if (not Q1.isEmpty()):
            print(Q1.deQueue())
        else:
            print("Empty")
    elif('ES' in i):
        Q2.enQueue(i.replace('ES ',''))



