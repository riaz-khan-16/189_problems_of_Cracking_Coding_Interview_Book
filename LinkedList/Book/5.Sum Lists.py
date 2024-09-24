# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode()
        carry=0
        current=head
        while l1 and l2:
            current.next=ListNode((l1.val+l2.val+carry)%10)
            carry=(l1.val+l2.val+carry)//10
            l1=l1.next
            l2=l2.next
            current=current.next
        while l1:
            current.next=ListNode((l1.val+carry)%10)
            carry=(l1.val+carry)//10
            l1=l1.next
            current=current.next
        while l2:
            current.next=ListNode((l2.val+carry)%10)
            carry=(l2.val+carry)//10
            l2=l2.next
            current=current.next
        while carry:
            current.next=ListNode(carry%10)
            carry=carry//10
            current=current.next

        return head.next
