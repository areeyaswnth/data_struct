
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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
#AP I,AP Love,AP KMITL,AP 2020
    def append(self, item):
        newNode = Node(item);    
        if(self.head == None):    
            self.head = self.tail = newNode;    
            self.head.previous = None;     
            self.tail.next = None;    
        else:      
            self.tail.next = newNode;    
            newNode.previous = self.tail;    
            self.tail = newNode;    
            self.tail.next = None;  
        self.Size +=1  



    def addHead(self, item):
        new = Node(item)
        if L.isEmpty() :
            self.head = new
            self.tail = new
        else :
            current = self.head
            new.next = self.head
            current.previous = new
            self.head = new
            while current.next != None :
                current = current.next
            self.tail = current
        self.Size +=1  

        # p = Node(item)
        # if self.head==None:
        #     self.head = self.tail = p;    
        #     self.head.previous = None;     
        #     self.tail.next = None; 
        #     self.tail.previous=self.head   
        #     self.Size+=1  
            
        # else:
        #     p.next = self.head
        #     self.head = p
        #     self.head.previous=None
        #     self.Size+=1
        #     # self.tail.next = newNode;    
        #     # newNode.previous = self.tail;    
        #     # self.tail = newNode;    
        #     # self.tail.next = None;  
            

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
        return self.Size

    def pop(self, pos):
        t = self.head
        count = 0
        if pos == 0 and t != None:
            self.head = None
            self.Size-=1
            return "Success"
        while t != self.tail:
            if count == int(pos)-1:
                t.next=t.next.previous

                self.Size-=1
                return "Success"
            count += 1
            t = t.next
        # # self.tail=t
        # print(self.tail.value)
        del t, count
        return "Out of Range"
    # def insert(self, index ,data):
    def insert(self, pos, item):
        new = Node(item)
        if L.isEmpty() :
            self.head = new
            self.tail = new
        else :
            current = self.head
            if pos < 0 and -pos < L.size():
                for _ in range(L.size() - 1 + pos) :
                    current = current.next
            elif -pos >= L.size() :
                self.addHead(new.value)
                return
            elif pos > L.size() :
                self.append(new.value)
                return
            else :
                for _ in range(pos-1) :
                    current = current.next
            new.next = current.next
            new.previous = current
            current.next = new
            current = new
            if current.next != None :
                current = current.next
                current.previous = new
            while current.next != None :
                current = current.next
            self.tail = current
        self.Size+=1

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
print("Linked List Reverse :", L.reverse())