# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
head=Node(5,Node(4,Node(2,Node(1))))

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
   
first,second=first,prev
max_sum=0

while first and second:
    temp1,temp2=first.next,second.next
    max_sum=max(first.data+ second.data, max_sum)
    first,second=temp1, temp2


print(max_sum)

