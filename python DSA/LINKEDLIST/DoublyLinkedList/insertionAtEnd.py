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

#Insertion At End my code and actual are same, time: O(n) and space:O(1)
def addLast(last,data):
    new_node = Node(data)

    if last is None:
        head = new_node
        return
    
    while last.next is not None:
        last = last.next
    
    last.next = new_node
    new_node.prev = last

addLast(head,100)

#Display Code
temp = head
while temp!=None:
    print(temp.data,end=' ')
    temp=temp.next
print()