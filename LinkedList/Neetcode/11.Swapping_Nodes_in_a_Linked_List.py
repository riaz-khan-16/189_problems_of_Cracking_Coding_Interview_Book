#https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/



class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
head=Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
k=2


# First pass: find the length of the linked list
length = 0
current = head
while current:
    length += 1
    current = current.next

# Identify the kth node from the start and the kth node from the end
first = head
for _ in range(k - 1):
    first = first.next

second = head
for _ in range(length - k):
    second = second.next

# Swap the values of the two nodes
first.val, second.val = second.val, first.val

print(head.val)




