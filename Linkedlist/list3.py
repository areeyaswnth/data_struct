

class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        print()


def createList(l=[]):
    p = node(int(l[0]), None)
    Head = p
    for i in range(1, len(l)):
        p.next = node(int(l[i]), None)
        p = p.next
    return Head


def printList(H):
    while (H != None):
        print(H.data, '', end='')
        H = H.next
    print()


def mergeOrderesList(p, q):
    ### Code Here ###
    l = []
    while p != None or q != None:
        if p == None:
            l.append(q.data)
            q = q.next
        elif q== None:
            l.append(p.data)
            p = p.next
        elif p.data <= q.data:
            l.append(p.data)
            p = p.next    
        elif p.data > q.data:
            l.append(q.data)
            q = q.next       
    return createList(l)


#################### FIX comand ####################
# input only a number save in L1,L2
inp = input('Enter 2 Lists : ').split()
L1 = inp[0].split(',')
L2 = inp[1].split(',')
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('LL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('Merge Result : ', end='')
printList(m)
