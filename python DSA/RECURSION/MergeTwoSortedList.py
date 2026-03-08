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




temp1 =  head
temp2 = head2
if temp1.val>temp2.val:
        t = temp2
        temp2=temp2.next
else:
        t=temp1
        temp1=temp1.next
merged = t



if temp1 == None:
    merged = head2
    traverseList(head2)
elif temp2 == None:
    merged= head1
    traverseList(head1)
else:
    
    def Merged(t):
            global temp1
            global temp2
            global merged
            if temp1 != None and temp2 != None:

                if temp1.val > temp2.val:
                        t.next = temp2
                        temp2 = temp2.next
                        return Merged(t.next)
                else:
                        t.next = temp1
                        temp1 = temp1.next
                        return Merged(t.next)
            else:
                if temp1 == None:
                    t.next=temp2
                    return merged
                else:
                    t.next=temp1
                    return merged
        
    traverseList(Merged(t))