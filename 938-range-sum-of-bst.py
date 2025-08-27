# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        def subtree(root,low,high):
            if not root:
                return 0
            current_sum=0
            if root.val>=low and root.val<=high:
                current_sum+=root.val
            left_subtree=subtree(root.left,low,high)
            right_subtree=subtree(root.right,low,high)
            return current_sum+left_subtree+right_subtree
        return subtree(root,low,high)  