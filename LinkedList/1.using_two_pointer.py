from Creating_Singly_Linked_list import Node, Linkedlist


L=Linkedlist()   #initializing Linked List
L.head=Node(1)  #giving the head value using Node()
L.head.next=Node(5)
L.head.next.next=Node(6)
L.head.next.next.next=Node(9)
L.head.next.next.next.next=Node(5)
L.head.next.next.next.next.next=Node(0)
L.head.next.next.next.next.next.next=Node(3)

L.printNode()
                                              

current=L.head                                    

while current is not None:                       
    runner=current                                  
    while runner.next is not None:             
        if runner.next.data==current.data:     
            runner.next=runner.next.next       

        else:
            runner=runner.next                
    current=current.next                       



L.printNode()