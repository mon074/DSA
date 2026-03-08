# constructor to initialize a new node with data
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Create the first node (head of the list)
head = Node(10)

# Link the second node
head.next = Node(20)

# Link the third node
head.next.next = Node(30)

# Link the fourth node
head.next.next.next = Node(40)

#ITERATIVE
# function to traverse and print the singly linked list
def traverseList(head):
    while head is not None:
        print(head.data, end="")
        if head.next is not None:   
            print(" -> ", end="")
        head = head.next
    print()

#RECURSIVE
# function to traverse and print the singly linked list
def traverseList(head):
    # base condition is when the head is None
    if head is None:
        print()
        return

    # printing the current node data
    print(head.data, end="")

    # print arrow if not the last node
    if head.next is not None:
        print(" -> ", end="")

    # moving to the next node
    traverseList(head.next)