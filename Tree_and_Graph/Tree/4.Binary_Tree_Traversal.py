class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Example binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# in order traversal

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.key)
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print(root.key)
        in_order_traversal(root.left)
        in_order_traversal(root.right)

pre_order_traversal(root)




