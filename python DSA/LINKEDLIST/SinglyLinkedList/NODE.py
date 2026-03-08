# constructor to initialize a new node with data
class Node:
    def __init__(self, new_data):
        self.new_data = new_data
        self.next = None

# Create the first node (head of the list)
head = Node(10)

# Link the second node
head.next = Node(20)

# Link the third node
head.next.next = Node(30)

# Link the fourth node
head.next.next.next = Node(40)

