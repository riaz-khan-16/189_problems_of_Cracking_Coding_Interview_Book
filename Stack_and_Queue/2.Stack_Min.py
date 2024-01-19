

# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.




#at first create an stack using array:

class stack:
    def __init__(self):
            self.stack=[]
            self.min=[]
    def push(self,data):
          self.stack.append(data)
          if len(self.min)==0:
                self.min.append(data)
          else:        
              if data<self.min[-1]:
                    self.min.append(data)


    def pop(self):
          last=self.stack[-1]
          if self.stack:
             self.stack.pop(-1)
             if last==self.min[-1]:
                   self.min.pop(-1)

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
          print('stack:'+str(self.stack)+' Min:'+ str(self.min[-1])) 
          
s=stack()
s.push(5)
s.push(6)
s.push(7)
s.push(3)
s.pop()
s.pop()
s.pop()
s.peek()

s.is_empty()

s.display()









    


