class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create the first node (head of the list)
head = Node(1)

# Link the second node
head.next = Node(2)

# Link the third node
head.next.next = Node(6)

# Link the fourth node
head.next.next.next = Node(3)

head.next.next.next.next= Node(4)

head.next.next.next.next.next= Node(5)


head.next.next.next.next.next.next= Node(6)

def traverseList(head):
    while head is not None:
        print(head.val, end="")
        if head.next is not None:   
            print(" -> ", end="")
        head = head.next
    print()


target = head
traverseList(target)
prev=None
after=None
val=6

while target!=None:
    
    if target.val!=val:
        prev=target
        target = target.next
    else:
        
        if target.next!=None:
            after=target.next
        if prev == None:
            if after==None:
                head=None
                traverseList(head)
                break
            else:
                target.next = None
                target = after
                head=after
                after=None
        else:
            if after ==None:
                prev.next=None
                target=target.next
            else:
                prev.next=after
                target.next=None
                target=after
                after=None
    

traverseList(head)