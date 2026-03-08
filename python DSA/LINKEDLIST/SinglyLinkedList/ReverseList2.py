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

flag=1
ans=head
start=head

if head!=None:
    while head.next!=None:
        temp=head
        prev=head
        while temp.next!=None:
            temp=temp.next
            if temp.next!=None:
                prev=temp
        if start==head:
            temp.next=head
            prev.next=None
        else:
            start.next=temp
            temp.next=head
            prev.next=None
        start=temp
        if flag==1:
            flag=0
            ans=start
    traverseList(ans)
else:
    traverseList(ans)