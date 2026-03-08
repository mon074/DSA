class Node:
    def __init__(self,data):

        self.prev=None
        self.data=data
        self.next=None

#Fisrt Node (head)
head = Node(10)

#Second Node 
head.next = Node(20)
head.next.prev=head

#third node 
head.next.next=Node(30)
head.next.next.prev=head.next

#fourth Node
head.next.next.next = Node(40)
head.next.next.next.prev= head.next.next

#My code time:O(n) and space:O(1)
def deleteE(end):
    if end is None:
        return
    if end.next is None:
        head = None
        return

    while end.next.next is not None:
        end = end.next

    end.next.prev = None
    end.next = None

deleteE(head)

#Display Code
temp = head
while temp!=None:
    print(temp.data,end=' ')
    temp=temp.next
print()