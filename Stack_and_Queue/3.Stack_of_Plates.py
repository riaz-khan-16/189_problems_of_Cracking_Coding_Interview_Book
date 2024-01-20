#Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack. 








class  set_of_stack:
    def __init__(self):
        self.set_of_stack=[[]]
        self.i=0
        self.limit=3
        self.current_stack= self.set_of_stack[self.i]
    def push(self,data):
        if len(self.current_stack)==self.limit:
            self.i=self.i+1
            self.set_of_stack.append([])  
            self.current_stack=self.set_of_stack[self.i]    
        self.current_stack.append(data)
            


    def display(self):
        print(self.set_of_stack) 

    def pop(self):
        if len(self.set_of_stack[-1])==0:
            self.set_of_stack.pop(-1)
        self.set_of_stack[-1].pop(-1)   
    def popAt(self,n):
        self.set_of_stack[n].pop(-1)


      

s=set_of_stack()
s.push(1)  
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(6)
s.push(7)
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
s.popAt(2)

s.display()     




        














    


