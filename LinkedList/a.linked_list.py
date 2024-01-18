
#create the basic linked List
class Node:
    def __init__(self,data, next=None):
        self.data=data
        self.next=next

linked_list = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60))))))   

  

def insertTail(head,newNode):
    if head.data is None:
        print(head)
        head=newNode
        print(head.data)
    else:
        current=head
        while current.next is not None:
            current=current.next
        current.next=newNode   
    return head        
    
         
linked_list=insertTail(linked_list,Node(1))






print(linked_list.next.data)
print(linked_list.next.next.data)
print(linked_list.next.next.next.data)
print(linked_list.next.next.next.next.data)
print(linked_list.next.next.next.next.next.data)
print(linked_list.next.next.next.next.next.next.data)
