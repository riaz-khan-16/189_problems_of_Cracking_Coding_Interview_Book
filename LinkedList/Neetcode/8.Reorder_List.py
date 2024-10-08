# https://leetcode.com/problems/reorder-list/

head = [1,2,3,4]

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
head=Node(1,Node(2,Node(3,Node(4))))

# at first we need to find the middle using slow and fast pointer

slow=head
fast=head.next
while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
second=slow.next
slow.next=None
first=head

#now reverse the second portion of the middle
prev=None
current=second
while current:
    temp=current.next
    current.next=prev
    prev=current
    current=temp
   

#Now merge the two list

first,second=first,prev

while second:
    temp1,temp2=first.next,second.next
    first.next=second
    second.next=temp1
    first,second=temp1,temp2


   






