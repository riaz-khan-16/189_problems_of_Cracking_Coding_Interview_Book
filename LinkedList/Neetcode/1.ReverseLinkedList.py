#https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.


class ListNode(object): 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head=ListNode(1,ListNode(2, ListNode(3)))

# class Solution(object):
def reverseList(head):
    current=head
    prev=None
    while current:
        temp=current.next
        current.next=prev
        prev=current
        current=temp
    return prev
