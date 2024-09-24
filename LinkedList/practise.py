class Node:
    def __init__(self,data, next=None):
        self.data=data
        self.next=next

linked_list = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60))))))   


#how to remove an element
#remove second element:

current=linked_list
c=1
while current.next:
    c=c+1
    if c==2:
        current.next=current.next.next
    current=current.next
   



