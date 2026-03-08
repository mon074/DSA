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

def traverseList(head):
    while head is not None:
        print(head.data, end="")
        if head.next is not None:   
            print(" -> ", end="")
        head = head.next
    print()



d={}
temp=head
i=1
while temp != None:
    d[i] = temp
    temp = temp.next
    i+=1
m = len(d)//2 +1
traverseList(d[m])