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

#Insertion At given pos my code and actual are same, time: O(n) and space:O(1)
def insertAtPos(head, pos, new_data):

    # Create a new node
    new_node = Node(new_data)

    # Insertion at the beginning
    if pos == 1:
        new_node.next = head

        # If the linked list is not empty, 
        # set the prev of head to new node
        if head is not None:
            head.prev = new_node

        # Set the new node as the head of linked list
        head = new_node
        return head

    curr = head
    # Traverse the list to find the node before the
    # insertion point
    for i in range(1, pos - 1):
        if curr is None:
            break
        curr = curr.next

    # If the position is out of bounds
    if curr is None:
        return head

    # Set the prev of new node to curr
    new_node.prev = curr

    # Set the next of new node to next of curr
    new_node.next = curr.next

    # Update the next of current node to new node
    curr.next = new_node

    # If the new node is not the last node, 
    # update prev of next node to new node
    if new_node.next is not None:
        new_node.next.prev = new_node

    # Return the head of the doubly linked list
    return head

head = insertAtPos(head, 3, 3)

#Display Code
temp = head
while temp!=None:
    print(temp.data,end=' ')
    temp=temp.next
print()