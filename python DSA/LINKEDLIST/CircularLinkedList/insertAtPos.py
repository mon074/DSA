class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)

head.next = Node(2)

head.next.next = Node(3)

head.next.next.next = head

#insert at a specific position
#if we know the last node then, time: O(n) and space: O(1)
#if we dont know the last node then, time: O(n^2) and space:O(1)
def insert_at_position(last, data, pos):
    if last is None:
        # If the list is empty
        if pos != 1:
            print("Invalid position!")
            return last
        # Create a new node and make it point to itself
        new_node = Node(data)
        last = new_node
        last.next = last
        return last

    # Create a new node with the given data
    new_node = Node(data)

    # curr will point to head initially
    curr = last.next

    if pos == 1:
        # Insert at the beginning
        new_node.next = curr
        last.next = new_node
        return last

    # Traverse the list to find the insertion point
    for i in range(1, pos - 1):
        curr = curr.next
        # If position is out of bounds
        if curr == last.next:
            print("Invalid position!")
            return last
    # Insert the new node at the desired position
    new_node.next = curr.next
    curr.next = new_node

    # Update last if the new node is inserted at the end
    if curr == last:
        last = new_node



#Print Function
def PrintList(head):
    temp = head

    while temp.next!=head:
        print(temp.data, end=' ')
        temp = temp.next

    print(temp.data)

PrintList(head)