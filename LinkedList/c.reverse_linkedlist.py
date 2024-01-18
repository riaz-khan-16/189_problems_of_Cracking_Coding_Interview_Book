

class Node:
    def __init__(self,data, next=None):
        self.data=data
        self.next=next

def display(head):
    l=''
    current=head
    while current is not None:
        l=l+str(current.data)+'->'
        current=current.next
    print(l)    

def insertAtHead(head,newNode):
    if head.data is None:
        head=newNode
        
    else:
        temp=head
        head=newNode
        head.next=temp
          
    return head


linked_list=Node(1,Node(2,Node(3,Node(4))))


def reverse_it(linked_list):
    reverse=Node(None)
    current=linked_list

    while True:
        if current is not None:
            reverse=insertAtHead(reverse,Node(current.data))
            current=current.next
        else:
            break    

    display(reverse)
    return reverse

reverse_it(linked_list)




    