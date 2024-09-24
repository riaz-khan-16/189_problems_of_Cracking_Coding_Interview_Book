# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
head=Node(1,Node(2,Node(3,Node(4,Node(5)))))
n=2
current=head
prev=None
while current:
    temp=current.next
    current.next=prev
    prev=current
    current=temp
head=prev
if n==1:
    head=head.next 
else:
    c=1
    current=head
    while current and current.next:
        c=c+1
        if c==n:
            current.next=current.next.next
        current=current.next

current=head
prev=None
while current:
    temp=current.next
    current.next=prev
    prev=current
    current=temp
print( prev)

    


