# https://leetcode.com/problems/reorder-list/

head = [1,2,3,4]

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
def insertAtHead(head,newNode):
    if head.data is None:
        head=newNode  
    else:
        temp=head
        head=newNode
        head.next=temp  
    return head
def reverese(list):
    reverse=Node(None)
    current=list
    while True:
        if current is not None:
            reverse=insertAtHead(reverse,Node(current.data))
            current=current.next
        else:
            break    
    return reverse
L=Node(1,Node(2,Node(3,Node(4))))
rev=reverese(L)
print(L.data)
temp=L.next
new=L
new.next=rev
new.next.next=temp




print(new.data,new.next.data,new.next.next.data)


