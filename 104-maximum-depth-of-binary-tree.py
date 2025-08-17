# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        def subtree(root):
            if not root:
                return 0
            left_subtree=subtree(root.left)+1
            right_subtree=subtree(root.right)+1
            return max(left_subtree,right_subtree)
        return subtree(root)
        