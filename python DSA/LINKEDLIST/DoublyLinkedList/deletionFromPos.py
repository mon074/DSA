class Node:
    def __init__(self,data):

        self.prev=None
        self.data=data
        self.next=None

# Fisrt Node (head)
head = Node(10)
# head = None

#Second Node 
head.next = Node(20)
head.next.prev=head

#third node 
head.next.next=Node(30)
head.next.next.prev=head.next

#fourth Node
head.next.next.next = Node(40)
head.next.next.next.prev= head.next.next


#My code time: O(n) space: O(1)
def deleteFromPos(pos):
    global head
    if head is None:
        return

    # Case 1: Delete head
    if pos == 1:
        head = head.next
        if head is not None:
            head.prev = None
        return

    # Traverse to the position
    curr = head
    pointer = 1
    while curr is not None and pointer < pos:
        curr = curr.next
        pointer += 1

    if curr is None:  # Position out of range
        return

    # Case 2: Delete middle or last node
    if curr.next is not None:
        curr.next.prev = curr.prev
    if curr.prev is not None:
        curr.prev.next = curr.next


deleteFromPos(1)


# #Actual code
# def delPos(head, x):
    
#     if head is None:
#         return head  

#     curr = head

#     # traverse to the node at the given position
#     for i in range(1, x):
#         if curr is None:
#             # position exceeds list length, no deletion
#             return head  
#         curr = curr.next

#     if curr is None:
#         # position exceeds list length, no deletion
#         return head  

#     # if the node to delete is not the first node
#     # update previous node's next
#     if curr.prev is not None:
#         curr.prev.next = curr.next

#     # if the node to delete is not the last node
#     # update next node's prev
#     if curr.next is not None:
#         curr.next.prev = curr.prev

#     # if deleting the head, move head pointer 
#     # to next node
#     if head == curr:
#         head = curr.next

#     del curr  # free memory of the deleted node
#     return head

# head = delPos(head, 2)
 
#Display Code
temp = head
while temp!=None:
    print(temp.data,end=' ')
    temp=temp.next
print()