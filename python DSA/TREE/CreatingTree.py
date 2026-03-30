# Node structure for tree
class Node:
    def __init__(self, x):
        self.data = x
        self.children = []

    

root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Function to add a child to a node
def addChild(parent, child):
    parent.children.append(child)

# Constructing tree
addChild(root, n2)
addChild(root, n3)
addChild(n2, n4)
addChild(n2, n5)

# Function to print parents of each node
def printParents(node, parent):
    if parent is None:
        print(str(node.data) + " -> NULL")
    else:
        print(str(node.data) + " -> " + str(parent.data))

    for child in node.children:
        printParents(child, node)

print("Parents of each node:")
printParents(root, None)


# Function to print children of each node
def printChildren(node):
    children_str = " ".join(str(child.data) for child in node.children)
    if children_str:
        print(str(node.data) + " -> " + children_str)
    else:
        print(str(node.data) + " -> NULL")
    for child in node.children:
        printChildren(child)


print("Children of each node:")
printChildren(root)

#printing leaf nodes
def printLeafNode(node):

    for child in node.children:
        printLeafNode(child)
    
    if not node.children:
        print(node.data)



print("Leaf nodes :")
printLeafNode(root)

#printing degree of each node
def printDegree(node):

    print(f"Degree of {node.data}: {len(node.children)}")

    for child in node.children:
        printDegree(child)

print("Degree of each node in a Tree:")
printDegree(root)