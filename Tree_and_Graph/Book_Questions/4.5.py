#Validate BST: Implement a function to check if a binary tree is a binary search tree. 


#traverse the tree

class Node:
  def __init__(self,value):
             self.value=value
             self.left=None
             self.right=None


root=Node(10)
root.left=Node(5)
root.right=Node(11)

def checkBST(root):
       if root:
              x=root.value
              if root.left:
                     if root.left.value<x:
                            return checkBST(root.left)
                     else:
                          return False
              if root.right:
                     if root.right.value>x:
                            return checkBST(root.right)
                     else:
                            return False       

       return True



print(checkBST(root))
