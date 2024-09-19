class Node:
    def __init__(self,data, next=None):
        self.data=data
        self.next=next

linked_list = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60))))))   
x=linked_list.next.next.next
x.next.next.next=Node(50)


print(linked_list.next.next.next.next.next.next.data)

