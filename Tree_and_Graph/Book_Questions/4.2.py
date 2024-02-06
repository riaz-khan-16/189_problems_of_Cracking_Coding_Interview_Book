# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm 
#              to create a binary search tree with minimal height


array=[1,2,3,4,5,6,7,8,9]


#create a binary tree

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None



def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        elif value > root.value:
            root.right = insert(root.right, value)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def tree_height(root):
    if root is None:
        return 0
    left_height=tree_height(root.left)
    right_height=tree_height(root.right)

    return max(left_height,right_height)+1







x=Node(1)
insert(x,2)
insert(x,3)
insert(x,4)
insert(x,5)


inorder_traversal(x)


