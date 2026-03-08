class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)

head.next = Node(2)

head.next.next = Node(3)

head.next.next.next = head

#delete at front
#if we know the last node then, time: O(1) and space: O(1)
#if we dont know the last node then, time: O(n) and space:O(1)
def delBegin(head):
    if head == None:
        return None

    elif head.next == head:
        return None
    
    else:

        last = head
        while last.next != head:
            last = last.next
        
        last.next = head.next
        head = head.next
        return head

head = delBegin(head)

#Print Function
def PrintList(head):
    temp = head

    while temp.next!=head:
        print(temp.data, end=' ')
        temp = temp.next

    print(temp.data)

PrintList(head)