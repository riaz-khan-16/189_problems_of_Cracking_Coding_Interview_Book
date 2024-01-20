# Sort Stack


#Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
#            an additional temporary stack, but you may not copy the elements into any other data structure
#            (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.



class Stack:
    def __init__(self):
        self.stack=[]
        self.temp=[]

    def peek(self):
        if self.stack:
           return self.stack[-1]
    
    def push(self,item):

        if self.stack:
            p=self.stack[-1]
            if p<item:
                while p<item and self.stack:
                    self.temp.append(p)
                    self.stack.pop() 
                    if self.stack: 
                        p=self.stack[-1]
            self.stack.append(item)
            while self.temp:
                self.stack.append(self.temp.pop())
        else:
            self.stack.append(item) 
                
            
s=Stack()
s.push(0)   

s.push(1)
print(s.stack)