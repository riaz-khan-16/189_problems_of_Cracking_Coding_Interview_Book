# #1st way to build a binary tree

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def print_tree(node):
#     if node is not None:
#         print_tree(node.left)
#         print(node.value)
#         print_tree(node.right)        

# # Example binary tree:
# #       1
# #      / \
# #     2   3
# #    / \
# #   4   5

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# print_tree(root)

# how to make a binary tree

# at first create a tmeplate

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
                
                         

                 
              