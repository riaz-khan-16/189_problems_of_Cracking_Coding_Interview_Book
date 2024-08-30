
from LinkedList.bSinglyLinkedList import Node, Linkedlist



l=Linkedlist()
l.head=Node(1)
l.head.next=Node(5)
l.head.next.next=Node(7)
l.head.next.next.next=Node(8)
l.head.next.next.next.next=Node(6)



x=set([])
l.printNode()

prevNode=None
currentNode=l.head
print(currentNode.data)

while currentNode is not None:
    if currentNode.data not in x:
        x.add(currentNode.data)
        prevNode=currentNode
        
    else:
        prevNode.next=currentNode.next
    currentNode=currentNode.next

l.printNode()



