class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head = None


def createLL(LL):

    p = Node(int(LL[0]))
    L.head = p
    for i in range(1, len(LL)):
        p.next = Node(int(LL[i]))
        p = p.next
    return L.head

def printLL(head):
    str1=''
    while (head != None):
        str1=str1+str(head.value)+' '

        head = head.next
    return str1


def SIZE(head):
    size=0
    while (head != None):
        size+=1
        head = head.next
    return size
    # Code Here

def scarmble(head, b, r, size):
    h1=BottomUp(head,b,size)
    h2=Riffle(h1,r,size)
    h3=head
    if(r>=60):
        h3=Deriffle(h2,r,size)
        h4=Debottomup(h3,b,size)
    else:
        h3=Deriffle2(h2,r,size)
        h4=Debottomup(h3,b,size)
    return printLL(head)
    # Code Here
def BottomUp(head,b,size):
    p=head
    n=size*b//100
    c=1
    t=head
    while (head != None):
        if(c==n):
            p=head.next
            head.next=None
        c+=1
        head = head.next 
    head=p
    while (head.next != None):
        head=head.next
    head.next=t
    head=p
    print('BottomUp',format(b,".3f"),'%',':',printLL(head))   
    return head

def Riffle(head,r,size):
    n=size*r//100
    p=head
    c=1
    t=head
    while (head != None):
        if(c==n):
            p=head.next
            head.next=None
        c+=1
        head = head.next 
    head=t
    
    while (head.next != None):
        if(p != None):
            temp=p.next
            p.next=head.next
            head.next=p
            p=temp
            head=head.next
        head=head.next
    if(p!=None):
        head.next=p
    head=t
    print('Riffle',format(r,".3f"),'%',':',printLL(head)) 

    return head

def Deriffle(head,r,size):
    n=size-(size*r//100)
    p=None
    p2=None
    c=1
    t=head
    pH=None
    while (head != None ):
        if c%2==0 and n>0:
            if(p!=None):
                p.next = head
            else:
                pH=head
            p=head
            n-=1
        elif(c%2==1 or (c%2==0 and n<0)):
            
            if(p2!=None):
                p2.next=head
            p2=head
        c+=1
        head=head.next
        if(n==0):
            p.next=None
            n=-1
    head=t
    while head.next != None:
        
        head=head.next
    head.next=pH
    print('Deriffle',format(r,".3f"),'%',':',printLL(t)) 
    return t

def Deriffle2(head,r,size):
    n=(size*r//100)
    p=None
    p2=None
    c=1
    t=head
    pH=None
    while (head != None ):
        if c%2==0 or (c%2==1 and n<0):
            if(p!=None):
                p.next = head
            else:
                pH=head
            p=head
        elif(c%2==1 and n>0):
            if(p2!=None):
                p2.next=head
            p2=head
            n-=1
        c+=1
        head=head.next
        if(n==0):
            p2.next=None
            n-=1
    head=t
    while head.next != None:
        head=head.next
    head.next=pH        
    print('Deriffle',format(r,".3f"),'%',':',printLL(t)) 
    return t
def Debottomup(head,b,size):
    p=head
    pH=None
    n=size-(size*b//100)
    c=1
    t=head
    while (head != None):
        if(c==n):
            p=pH=head.next
            head.next=None
        c+=1
        head=head.next
    while(p.next!=None):
         p=p.next
    p.next=t
    p=pH
    print('Debottomup',format(b,".3f"),'%',':',printLL(p))  
    return t


    
L=LinkedList()    
inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)
