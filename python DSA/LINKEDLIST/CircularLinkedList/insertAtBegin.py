class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)

head.next = Node(2)

head.next.next = Node(3)

head.next.next.next = head

#Insert at  front
#if we know the last node then, time: O(1) and space: O(1)
#if we dont know the last node then, time: O(n) and space:O(1)

def inserAtBegin(head,key):
    
    new = Node(key)
    last = head

    if head is not None:

        while last.next!=head:
            last=last.next
        
        new.next = head
        last.next = new
        head = new
        return head

    else:
        head = new
        new.next = new
        return head

head = inserAtBegin(head,0)


#Print Function
def PrintList(head):

    temp = head

    while temp.next!=head:
        print(temp.data, end=' ')
        temp = temp.next

    print(temp.data)

PrintList(head)