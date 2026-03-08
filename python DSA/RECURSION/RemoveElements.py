class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create the first node (head of the list)
head = Node(6)

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


# target = head
# traverseList(target
prev=None

val=6

def RemoveEl(target):
    global prev
    after=None
    global head
    
    if target==None:
        return head

    if target.next!=None:
        after=target.next

    if target.val==val:
        if prev == None:
            if after == None:
                return None
            else:
                target.next=None
                head = after
                target=after
                return RemoveEl(target)
        else:
            if after==None:
                prev.next=None
                target=None
                return RemoveEl(target)
            else:
                prev.next=after
                target.next=None
                target=after
                return RemoveEl(target)
    else:
        prev=target
        return RemoveEl(target.next)

RemoveEl(head)
traverseList(head)