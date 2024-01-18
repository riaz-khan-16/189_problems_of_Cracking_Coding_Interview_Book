class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

Linklist=Node(1,Node(2,Node(3)))   
Linklist.next.next.next=Linklist


x=0
while True:
    print(Linklist.data)
    Linklist=Linklist.next
    x=x+1
    if x==20:
        break


