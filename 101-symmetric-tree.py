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