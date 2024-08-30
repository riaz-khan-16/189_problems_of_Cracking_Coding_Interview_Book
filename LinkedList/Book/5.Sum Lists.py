# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912. 



class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next  


def insertTail(head,newNode):
    if head.data is None:
        
        head=newNode
       
    else:
        current=head
        while current.next is not None:
            current=current.next
        current.next=newNode   
    return head 

A=Node(1,Node(2,Node(9)))   
B=Node(2,Node(9,Node(6)))   

result=Node()
carry=0

while True:
    if A is not None and B is not None :
        sum=(A.data+B.data+carry)
        r=sum%10
        result=insertTail(result,Node(r))
        carry=sum//10
        A=A.next
        B=B.next
    elif A is not None and B is None:
        sum=(A.data+carry)
        r=sum%10
        result=insertTail(result,Node(r))
        carry=sum//10
        A=A.next

    elif B is not None and A is None:
        sum=(B.data+carry)
        r=sum%10
        result=insertTail(result,Node(r))
        carry=sum//10
        B=B.next  

    elif carry:
            sum=(carry)
            r=sum%10
            result=insertTail(result,Node(r))
            break
    else:
        break          
        


print(result.data)
print(result.next.data)
print(result.next.next.data)
print(result.next.next.next.data)
       




            






 

 
 


