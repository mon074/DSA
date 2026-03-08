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


#My code time:O(1) and Space:O(1)

def deleteF(head):

    if head is None:
        return head
    
    head = head.next
    head.prev = None
    return head

head = deleteF(head)

#Display Code
temp = head
while temp!=None:
    print(temp.data,end=' ')
    temp=temp.next
print()