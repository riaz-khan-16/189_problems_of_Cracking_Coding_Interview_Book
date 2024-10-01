#https://leetcode.com/problems/swap-nodes-in-pairs/description/

class Node:
    def __init__(self, val,next=None):
        self.val=val
        self.next=next
head=Node(1,Node(2,Node(3,Node(4))))

def display(head):
    arr=[]
    current=head
    while current:
        arr.append(current.val)
        current=current.next
    print(arr)


dummy=Node(0,head)
prev=dummy
curr=head
while curr and curr.next:
    nxtPair=curr.next.next
    second=curr.next
    curr.next=nxtPair
    second.next=curr
    prev.next=second

    prev=curr
    curr=nxtPair

display(dummy.next)








