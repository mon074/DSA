class Node:
    def __init__(self, data):
        self.data = data
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


arr=[]
temp=head
while temp!=None:
    arr.append(temp)
    temp=temp.next
temp=arr[-1]
head=temp
for i in range(len(arr)-1,-1,-1):
    temp.next=arr[i]
    temp=temp.next
temp.next=None


traverseList(head)