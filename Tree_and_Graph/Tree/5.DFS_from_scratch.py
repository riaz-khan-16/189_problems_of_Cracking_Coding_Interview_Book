# DFS from Scrath


# Binary Tree


class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None


#          A
#     B          C
# B1    B2     C1   C2   

tree=Node('A')
tree.left=Node('B')
tree.left.left=Node('B1')
tree.left.right=Node('B2')

tree.right=Node('C')
tree.right.left=Node('C1')
tree.right.right=Node('C2')


#In DFS the output should be B1 B B2 A C1 C C2


def DFS(root):
    if root:
        DFS(root.left) 
        print(root.value) 
        DFS(root.right)
DFS(tree)

