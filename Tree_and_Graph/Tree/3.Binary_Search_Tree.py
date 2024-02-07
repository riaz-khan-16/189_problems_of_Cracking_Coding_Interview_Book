# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# def insert(root, key):
#     if root is None:
#         return TreeNode(key)
#     else:
#         if key < root.key:
#             root.left = insert(root.left, key)
#         elif key > root.key:
#             root.right = insert(root.right, key)
#     return root

# def search(root, key):
#     if root is None or root.key == key:
#         return root
#     if key < root.key:
#         return search(root.left, key)
#     return search(root.right, key)

# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.key, end=" ")
#         inorder_traversal(root.right)

# # Example usage:
# root = None
# keys = [50, 30, 20, 40, 70, 60, 80]

# for key in keys:
#     root = insert(root, key)

# print("Inorder Traversal:")
# inorder_traversal(root)

# # Search for a key
# search_key = 40
# result = search(root, search_key)
# if result:
#     print(f"\nKey {search_key} found in the tree.")
# else:
#     print(f"\nKey {search_key} not found in the tree.")


# make a class or template

class BST:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def insert(root,new):
    if root is None:
        return BST(new)
    if new>root.value:
        root.right= insert(root.right,new)
    if new<root.value:
        root.left=insert(root.left,new)
    return root

def print_tree(root):
    if root:
        print_tree(root.left) 
        print(root.value) 
        print_tree(root.right)

#          5
#     B          C
# B1    B2     C1   C2   

tree=BST(0)
for i in range(5):
    insert(tree,i)


print_tree(tree)