class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)
# head.next = head

head.next = Node(2)

head.next.next = Node(3)
last = head.next.next

last.next = head


#del from pos
#time: O(n) and space: O(1)
def deleteSpecificNode(head, key):
    global last

    if head is None:
        return None

    curr = head
    prev = last

    # If the node to be deleted is the only node in the list
    if curr.next == head and curr.data == key:
        head = None
        return head

    # If the node to be deleted is the first node
    if curr.data == key:
        head = head.next
        last.next = head
        return head

    # Traverse the list to find the node to be deleted
    while curr != last and curr.data != key:
        prev = curr
        curr = curr.next

    # If the node to be deleted is found
    if curr.data == key:
        prev.next = curr.next
        # if curr == head:
            # head = prev

    return head

head = deleteSpecificNode(head, 1)

#Print Function
def PrintList(head):
    temp = head

    if head is None:
        print("empty list")
        return

    while temp.next!=head:
        print(temp.data, end=' ')
        temp = temp.next

    print(temp.data)

PrintList(head)