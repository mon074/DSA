class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)
# head.next = head

head.next = Node(2)

head.next.next = Node(3)
last = head.next.next


#del from end
#time: O(n) and space: O(1)

def deleteLastNode(head):
    global last

    if head is None:
        return None


    # If there is only one node in the list
    if head == last:
        return None

    # Traverse to find the second last node
    curr = head
    while curr.next != last:
        curr = curr.next

    # Update pointers
    curr.next = head
    last = curr

    return head

head = deleteLastNode(head)


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