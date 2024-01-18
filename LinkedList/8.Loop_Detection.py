

# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input:

# A -> B -> C -> D -> E -> C [the same C as earlier]
# Output:
# C
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

Linklist=Node(1,Node(2,Node(3,Node(4))))   
Linklist.next.next.next.next=Linklist

current=Linklist
while current is not None:
    
    
    if current.next==Linklist:
        print(current.data)
        break
    else:
        current=current.next
    