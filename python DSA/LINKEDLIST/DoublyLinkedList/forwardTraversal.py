class Node:
    def __init__(self,data):

        self.prev=None
        self.data=data
        self.next=None

#Fisrt Node (head)
head = Node(10)

#Second Node 
head.next = Node(20)
head.next.prev=head

#third node 
head.next.next=Node(30)
head.next.next.prev=head.next

#fourth Node
head.next.next.next = Node(40)
head.next.next.next.prev= head.next.next


#My iterative approach and actual are same
#time complexity: O(n) and Auxilliary Space: O(1)
temp = head
while temp!=None:
    print(temp.data,end=' ')
    temp=temp.next
print()

#My recursive approach and actual same
#time complexity: O(n) and Auxilliary Space: O(n)
def traverseList(temp):
    if temp==None:
        print()
        return
    print(temp.data,end=' ')
    return traverseList(temp.next)

traverseList(head)

