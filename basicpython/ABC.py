
print('*** Reading E-Book ***')
print('Text , Highlight :',end='')
book=input()
p=book[len(book)-1]
for n in range(0,len(book)-2):
    if(book[n]==p):
        print('[',book[n],']',sep='',end='')
    else:
        print(book[n],sep='',end='')

