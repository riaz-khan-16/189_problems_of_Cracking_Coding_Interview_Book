#https://leetcode.com/problems/remove-linked-list-elements/description/
#203. Remove Linked List Elements

head = [1,2,6,3,4,5,6], val = 6

#removing an element
while head is not None and head.val==val:
    head=head.next
x=head
while x is not None and x.next is not None:
    if x.next.val==val:
        x.next=x.next.next
    x=x.next



    


