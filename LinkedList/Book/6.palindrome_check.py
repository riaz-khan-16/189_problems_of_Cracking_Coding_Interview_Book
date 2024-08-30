
#Palindrome: Implement a function to check if a linked list is a palindrome. 


class  Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

Linkedlist=Node(1,Node(2,Node(3,Node(2,Node(1)))))    

def insertAtHead(head,newNode):
    if head is None:
        head=newNode
    else:
        temp=head
        head=newNode
        head.next=temp   
    return head    

def reverse_it(head):
    reverse=Node()
    current=head
    while current is not None:
        x=current.data
        reverse=insertAtHead(reverse,Node(x))
        current=current.next

    return reverse    
reverse=reverse_it(Linkedlist)

def is_equal(list1,list2):
    list1=list1
    list2=list2
    while list1 is not None and list2 is not None:
                d1=list1.data
                d2=list2.data
                if d1==d2:
                     list1=list1.next
                     list2=list2.next
                else:
                     return False 
                     break
    return True                


print(is_equal(reverse, Linkedlist))

