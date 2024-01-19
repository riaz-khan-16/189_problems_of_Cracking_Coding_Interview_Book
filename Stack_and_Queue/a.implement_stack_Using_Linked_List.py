# 1. Implement using a linkedlist
# 2. Implement by an array
# a stack has four method:
#                        1.push(item)   -add item  at the top of the stack
#                        2.pop()        -remove the top iteme
#                        3.peek()       -return the top item
#                        4.is_empty()   -check the stack is empty or not



class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

class Stack:  

    def __init__(self):
        self.top=None


    def push(self,data):
        if self.top is None:
            self.top=Node(data)
        else:
            new=Node(data)
            new.next=self.top
            self.top=new

    def peek(self):
        if self.top is None:
            return None
        else:
            print(self.top.data)
        return self.top.data    

    def pop(self):
        if self.top is None:
            return False
        else:    
            self.top=self.top.next
    
    def is_empty(self):
        if self.top is None:
            print('Empty')
        else:
            print('Not Empty')    
        return self.top is None
    
    def display(self):
         current=self.top
         if current is None:
             print('No data in stack')

         else:
             d=''
             while  current is not None:
                d=d+str(current.data)+ ' <-'
                current=current.next   
             print(d)   

s=Stack()   
s.push(1)
s.push(2)     
s.push(3)    
s.peek()
s.is_empty()

s.display()









    