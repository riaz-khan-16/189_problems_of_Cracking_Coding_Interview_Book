class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class queue:
    def __init__(self):
        self.head=None
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def add(self,item):
        item=node(item)
        if self.head is None:
            self.head=item
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=item
       

    def remove(self):
        if self.head is not None:
            self.head=self.head.next

    def peek(self):
        pk=self.head
        if pk is not None:
            while pk.next is not None:
                pk=pk.next
            print(pk.data)    
            return pk.data    
        else:
            print(None)

       

    def display(self):
        current=self.head
        pri=''
        while current is not None:
            pri=pri+str(current.data)+'->'
            current=current.next
        print(pri+'None')




q=queue()
q.add(5)
q.add(6)
q.add(10)

q.peek()


q.display()



        

