# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks



class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self,item):
        self.stack1.append(item)

    def pop(self):
        while self.stack1:
            x=self.stack1.pop()
            self.stack2.append(x)
        p=self.stack2.pop()
        while self.stack2:
            y=self.stack2.pop()
            self.stack1.append(y)
        return p

x=Queue()
x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.push(5)
print(x.pop())
print(x.pop())
print(x.pop())
x.push(9)
print(x.stack1)


