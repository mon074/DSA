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

#Insertion Code mine 
# front = Node(0)
# front.next = head
# head.prev = front
# head = front

#Insertion at front Code actual , time: O(1) space: O(1)
def insert_at_front(head, new_data):
    # Create a new node
    new_node = Node(new_data)

    # Make next of new node as head
    new_node.next = head

    # Change prev of head node to new node
    if head is not None:
        head.prev = new_node

    # Return the new node as the head of the doubly linked list
    return new_node

data = 0
head = insert_at_front(head, data)

#Display Code
temp = head
while temp!=None:
    print(temp.data,end=' ')
    temp=temp.next
print()