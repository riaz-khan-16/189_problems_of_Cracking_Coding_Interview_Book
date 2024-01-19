

# using array:

class stack:
    def __init__(self):
            self.stack=[]
    def push(self,data):
          self.stack.append(data)
    def pop(self):
          if self.stack:
             self.stack.pop(-1)
          else:
                return None   
    def peek(self):
          print(self.stack[-1])
          return   self.stack[-1]      
    def is_empty(self):
          if len(self.stack)==0:
                print('yes')
                return True
          else:
                print('No')
        
    def display(self):
          print(self.stack) 
          
s=stack()
s.push(5)
s.push(6)
s.push(7)
s.peek()
s.pop()
s.is_empty()

s.display()









    


