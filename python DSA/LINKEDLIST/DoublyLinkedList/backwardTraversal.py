class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

# Create a hardcoded doubly linked list:
# 1 <-> 2 <-> 3
head = Node(1)
second = Node(2)
third = Node(3)
    
head.next = second
second.prev = head
second.next = third
third.prev = second
    
print("Backward Traversal: ")



#Iterative approach time:O(n) and auxilliary space: O(1)
def backwardTraversal(tail):
    curr = tail
    
    # Traverse the list in backward direction
    while curr is not None:
        # Output data of the current node
        print(curr.data, end=" ")
        
        # Move to the previous node
        curr = curr.prev
    print()
backwardTraversal(third)
  
#Recursive approach time:O(n) and auxilliary space: O(n)
def backward_traversal(node):
    if node is None:
        print()
        return

    # Print current node's data
    print(node.data, end=" ")
      	
    # Recursive call with the previous node
    backward_traversal(node.prev)

backward_traversal(third)