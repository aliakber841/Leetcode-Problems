# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def subtree(root,remaining):
            if not root:
                return False
            remaining=remaining-root.val
            if remaining==0 and (not root.left and not root.right):
                return True
            left_subtree=subtree(root.left,remaining)
            right_subtree=subtree(root.right,remaining)
            if left_subtree or right_subtree:
                return True
            return False
        return subtree(root,targetSum)
        