#Recursion

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

#time: order of n
#space: order of h (height of tree)
def inOrder(node, res):
    if node is None:
        return

    # Traverse the left subtree first
    inOrder(node.left, res)

    # Visit the current node
    res.append(node.data)

    # Traverse the right subtree last
    inOrder(node.right, res)

# Create binary tree
    #       1
    #      /  \
    #    2     3
    #   / \     \
    #  4   5     6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

res = []
inOrder(root, res)

print(res)