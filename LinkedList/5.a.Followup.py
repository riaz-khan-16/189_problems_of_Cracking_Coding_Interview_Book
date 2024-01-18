

class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next  

def insertAtHead(head,newNode):
    if head.data is None:
        head=newNode
        
    else:
        temp=head
        head=newNode
        head.next=temp
          
    return head        

def reverse_it(linked_list):
    reverse=Node(None)
    current=linked_list

    while True:
        if current is not None:
            reverse=insertAtHead(reverse,Node(current.data))
            current=current.next
        else:
            break    

  
    return reverse




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

A=reverse_it(A)
B=reverse_it(B)

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
        
result=reverse_it(result)

print(result.data,result.next.data, result.next.next.data)



