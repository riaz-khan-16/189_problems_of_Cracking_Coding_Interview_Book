

class Node:
    def __init__(self,data):
          self.data=data
          self.next=None

class Linkedlist:
     
     def __init__(self):
          self.head=None
          

     def insertAtTail(self,newNode):
          if self.head is None:
               self.head=newNode

          else:
               
               #find last node
               lastNode=self.head
               while True:
                    if lastNode.next is None:
                         break
                    lastNode=lastNode.next
               lastNode.next=  newNode

     def printNode(self):
          array=[]
          currentNode=self.head
          while True:
               if currentNode is None:
                    break
               array.append(currentNode.data)
               currentNode=currentNode.next
          print(array)

     def insertAtHead(self,newNode):
          temp=self.head  
          self.head=newNode
          self.head.next=temp
          del temp

     def insertAt(self,newNode,position):
          currentNode=self.head
          currentPos= 0
          while True:
               if currentPos==position:
                    prevNode.next=newNode
                    newNode.next=currentNode
                    break
               prevNode=currentNode
               currentNode=currentNode.next
               currentPos=currentPos+1


     def findLength(self):
          currentNode=self.head
          length=0
          while  currentNode is  not None:
               length+=1
               currentNode=currentNode.next
          return length      

     def  deleteLast(self):
          currentNode=self.head
          while True:
               if currentNode.next is None:
                    prevNode.next=None
                    del currentNode
                    break
               prevNode=currentNode
               currentNode=currentNode.next     


     def deleteAt(self,position):
          currentNode=self.head
          currentPos=0
          while True:
               if currentPos==position:
                    prevNode.next=currentNode.next
                    del currentNode
                    break
               prevNode=currentNode
               currentNode=currentNode.next
               currentPos+=1

     
                    


                  



               
# x=Node(5)
# y=Node(10)
# z=Node(15)
# m=Node(0)
# k=Node(634)




# a=Linkedlist()
# a.insert(x)
# a.insert(y)
# a.insert(z)
# a.insertAtHead(m)
# a.insertAt(k,2)


# a.deleteAt(2)
# a.printNode()

                  
          
        



