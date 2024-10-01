# https://leetcode.com/problems/rotate-list/description/

head = [1,2,3,4,5]
k = 2
def display(head):
    arr=[]
    current=head
    while current:
        arr.append(current.val)
        current=current.next
    print(arr)

class Node:
    def __init__(self, val,next=None):
        self.val=val
        self.next=next
head=Node(1,Node(2,Node(3)))
# head=Node(1,Node(2))
k=2000000000

def rotate(head):
    current=head

    if current.next:
        while current.next and current.next.next:
            current=current.next
        last=current.next
        current.next=None
        last.next=head
        return last
    return head
# find length of the list
current=head
length=0
while current:
    current=current.next
    length+=1
k=k%length

for i in range(k):
    head=rotate(head)
display(head)

 









    