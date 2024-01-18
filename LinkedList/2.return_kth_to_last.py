#Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.



class Node:
    def __init__(self,data, next=None):
        self.data=data
        self.next=next


linked_list = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60))))))        
k=3
def find_length(linked_list):

    current=linked_list
    length=0
    while current is not None:
        current=current.next
        length+=1
    return length   

length=find_length(linked_list)
req=length-k

current=linked_list
l=0
while current is not None:
    if l>=req:
        print(current.data)
    l=l+1    
    current=current.next   

    
    