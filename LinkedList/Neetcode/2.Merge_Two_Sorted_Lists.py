# https://leetcode.com/problems/merge-two-sorted-lists/description/

list1 = [1,2,4]
list2 = [1,3,4]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
list1=ListNode(1,ListNode(2,ListNode(4)))
list2=ListNode(1,ListNode(3,ListNode(4)))



res=ListNode()
current=res
while list1 and list2:
    if list1.val<list2.val:
        current.next=list1
        list1=list1.next
    else:
        current.next=list2
        list2=list2.next
    current=current.next
if list1:
    current.next=list1
if list2:
    current.next=list2

    

    

