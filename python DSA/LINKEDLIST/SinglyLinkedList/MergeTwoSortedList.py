class Node1:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create the first node (head of the list)
head = Node1(10)

# Link the second node
head.next = Node1(20)

# Link the third node
head.next.next = Node1(30)

# Link the fourth node
head.next.next.next = Node1(40)


class Node2:
    def __init__(self, val):
        self.val=val
        self.next = None

# Create the first node (head of the list)
head2 = Node2(10)

# Link the second node
head2.next = Node2(30)

# Link the third node
head2.next.next = Node2(50)


def traverseList(head):
    while head is not None:
        print(head.val, end="")
        if head.next is not None:   
            print(" -> ", end="")
        head = head.next
    print()


traverseList(head)
traverseList(head2)


temp1 = head
temp2 = head2
t = None
merged = None
flag=1

if temp1 == None:
    merged = head2
    traverseList(head2)
elif temp2 == None:
    merged= head
    traverseList(head)
else:
    while temp1 != None and temp2 != None:

        if temp1.val > temp2.val:
            if flag == 1:
                flag = 0
                merged = temp2
                temp2 = temp2.next
                # merged.next = None 
                # t = merged.next
                t=merged
            else:
                t.next = temp2
                temp2 = temp2.next
                # t.next = None
                t = t.next
        else:
            if flag == 1:
                flag = 0
                merged = temp1
                temp1 = temp1.next
                # merged.next = None
                # t = merged.next
                t=merged
            else:
                t.next = temp1
                temp1 = temp1.next
                t = t.next
    else:
        if temp1 == None:
            t.next=temp2
        else:
            t.next=temp1
traverseList(merged)
