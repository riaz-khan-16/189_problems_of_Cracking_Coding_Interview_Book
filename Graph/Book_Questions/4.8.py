# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_common_ancestor(root, node1, node2):
    if root is None:
        return None
    
    # If either node1 or node2 is the root, then root is the common ancestor
    if root == node1 or root == node2:
        return root
    
    # Recursively find the common ancestor in the left and right subtrees
    left_ancestor = find_common_ancestor(root.left, node1, node2)
    right_ancestor = find_common_ancestor(root.right, node1, node2)
    
    # If both left and right ancestors are not None, then root is the common ancestor
    if left_ancestor and right_ancestor:
        return root
    
    # Otherwise, return the non-None ancestor
    return left_ancestor if left_ancestor else right_ancestor

# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Find nodes
node1 = root.left.left  # Node with value 4
node2 = root.left.right  # Node with value 5

# Find the first common ancestor
ancestor = find_common_ancestor(root, node1, node2)
print("First common ancestor:", ancestor.value)  # Output should be 2

