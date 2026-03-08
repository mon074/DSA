class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
head=Node(20)
head.next=Node(30)
head.next.next=Node(50)

def traverse(h):
    temp=h
    while temp!=None:
        if temp.next!=None:
            print(temp.data,end='->')
        else:
            print(temp.data)
        temp=temp.next

traverse(head)

#AT FRONT
def AddInFront(h,num):
    newnode=Node(num)
    newnode.next=h
    h=newnode
    return h

#AT SOME POSITION
def AddAtPos(p,num,h):
    newnode= Node(num)
    i=1
    temp=h
    while i<p:
        prev=temp
        i+=1
        temp=temp.next
    prev.next=newnode
    newnode.next=temp
    return h

#ADD IN END
def AddInEnd(num,h):
    newnode=Node(num)
    temp=h
    while temp.next!=None:
        temp=temp.next
    temp.next=newnode
    return h
    




head = AddInFront(head,10)
head=AddAtPos(4,40,head)
head=AddInEnd(60,head)
traverse(head)