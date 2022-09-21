
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    
        self.head.next = self.tail
        # self.tail.previous = self.head
        self.Size=0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        self.Size+=1
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p

    def addHead(self, item):
        p = Node(item)
        p.next = self.head 
        self.head = p

    def insert(self, position, newElement): 
            newNode = Node(newElement)
            if(position < 1):
                print("\nposition should be >= 1.")
            elif (position == 1):
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            else:    
                temp = self.head
                for i in range(1, position-1):
                    if(temp != None):
                    temp = temp.next   
                if(temp != None):
                    newNode.next = temp.next
                    newNode.prev = temp
                    temp.next = newNode  
                    if (newNode.next != None):
                    newNode.next.prev = newNode
                else:
                    print("\nThe previous node is null.")  


    #     if(pos == self.Size):
    #         self.append(item)     
    #     if(pos == 0):
    #         self.head.previous = Node(item)
    #         self.head.previous.next = self.head
    #         self.head = self.head.previous
    #         self.Size += 1
    #     start = self.head
    #     for _ in range(pos):
    #         start = item.next
    #     start.previous.next = Node(item)
    #     start.previous.next.previous = start.previous
    #     start.previous.next.next = start
    #     start.previous = start.previous.next
    #     self.Size += 1
    # def insert(self,  index,data):
    #     # if (index > self.Size) | (index < 0):
    #     #     raise ValueError(f"Index out of range: {index}, size: {self.Size}")
             
    #     if(index == self.Size):
    #         self.append(data)
             
    #     if(index == 0):
    #         self.head.previous = Node(data)
    #         self.head.previous.next = self.head
    #         self.head = self.head.previous
    #         self.count += 1
         
    #     start = self.head
    #     for _ in range(index):
    #         start = start.next
    #     start.previous.next = Node(data)
    #     start.previous.next.previous = start.previous
    #     start.previous.next.next = start
    #     start.previous = start.previous.next
    #     self.Size += 1


    def search(self, item):
        found = False
        current_node = self.head
        while current_node != None :
            if current_node.value == item :
                found = True
                break
            else:
                current_node = current_node.next
        if(found):
            return "Found"
        else:
            return "Not Found"

    def index(self, item):
        C=0
        current = self.head
        while current != None:
            
            if current.value == item:
                return C
            else:
                current = current.next
            C+=1
        if current == None:
            return -1
        print ("item not present in list")

    def size(self):
        return str(self.Size)


    def pop(self, pos):
        t = self.head
        count = 0
        if pos == 0 and t != None:
            self.head = None
            return "Success"
        while t != None:
            if count == int(pos)-1:
                if t.next == None:
                    return "Out of Range"
                elif t.next.next == None:
                    t.next == None
                    return "Success"
                elif t.next.next != None:
                    t.next = t.next.next
                    return "Success"
            count += 1
            t = t.next
        del t, count
        return "Out of Range"
        #Code Here

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
#print("Linked List Reverse :", L.reverse())