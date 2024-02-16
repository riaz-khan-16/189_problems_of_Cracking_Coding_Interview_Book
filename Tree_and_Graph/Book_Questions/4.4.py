#Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
#this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
#node never differ by more than one.


def getheight(root):
    if not root:
        return -1
    if root:
        return max(getheight(root.left),getheight(root.right))+1
def isBalanced(root):
    if not root:
        return True
    heightDiff=getheight(root.left)-getheight(root.right)
    if heightDiff>1:
        return False
    else:
        isBalanced(root.left) and isBalanced(root.right)
        