

class Node:
    def __init__(self,value):
           self.value=value
           self.right=None
           self.left=None
    def insert_left(self, new):
           new=Node(new)
           self.left=new
    def insert_right(self, new):
           new=Node(new)
           self.right=new    

    #          A
    #        /   \
    #     B        C
    #    /  \     /  \
    #  B1    B2   C1  C2
           

           
tree=Node('A')
tree.insert_left('B')
tree.insert_right('C')

tree.left.insert_left('B1')
tree.left.insert_right('B2')

tree.right.insert_left('C1')
tree.right.insert_right('C2')



def display(root):
      if root:
            print(root.value)
      if root.right:
            display(root.right)
      if root.left:
            display(root.left)      
                  


display(tree)

                         

                 
              