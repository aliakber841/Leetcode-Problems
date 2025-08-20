# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        def subtree(root):
            if not root:
                return 0
            left_subtree=subtree(root.left)
            right_subtree=subtree(root.right)
            if left_subtree==0 or right_subtree==0:
                return max(left_subtree,right_subtree)+1
            else:
                 return 1+min(left_subtree,right_subtree)
        return subtree(root)
        