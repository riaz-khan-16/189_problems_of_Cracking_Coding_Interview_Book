# https://leetcode.com/problems/partition-list/description/
def display(head):
    arr=[]
    current=head
    while current:
        arr.append(current.val)
        current=current.next
    print(arr)

# Node class
class Node:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next
head=Node(1,Node(4,Node(3,Node(2,Node(5,Node(2))))))
display(head)
x=3

# need to partision

res=Node(0)
res_cur=res
current=head
# First loop: Add nodes with val < x
while current:
    temp=current
    if current.val < x:
        res_cur.next = Node(temp.val) # Append current node to the result list
        res_cur = res_cur.next  # Move to the next node in the result list
    current = current.next

display(head)
display(res)
current=head
while current:
    
    if current.val>=x:
        res_cur.next=Node(current.val)
        res_cur=res_cur.next
    current=current.next
display(res)