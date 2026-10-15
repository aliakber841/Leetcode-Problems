# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def compare(left,right):
    if left is None and right is None:
        return True
    elif left is None or right is None:
        return False
    elif left.val!=right.val:
        return False
    return compare(left.left,right.right) and compare(left.right,right.left)
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return compare(root.left,root.right)
    
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def subtree(left_root,right_root):
            if not left_root and not right_root:
                return True
            elif not left_root or not right_root:
                return False
            elif left_root.val!=right_root.val:
                return False
            return subtree(left_root.left,right_root.right) and  subtree(left_root.right,right_root.left)
        return subtree(root.left,root.right)