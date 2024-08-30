class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#At first we will create a link list
Linklist=Node(1,Node(2,Node(3)))   


#Then we will connect the last node to the head
Linklist.next.next.next=Linklist

# Traversing linkedlist untill 20 data is diplayed
x=0
while True:
    print(Linklist.data)
    Linklist=Linklist.next
    x=x+1
    if x==20:
        break


