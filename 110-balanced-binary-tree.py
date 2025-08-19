# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        def subtree(root):
            if not root:
                return (0,True)
            left_height,left_balanced=subtree(root.left)
            right_height,right_balanced=subtree(root.right)
            height=1+max(left_height,right_height)
            balanced= (left_balanced and right_balanced) and (
                abs(left_height-right_height)<=1
            )
            return (height,balanced)
        return subtree(root)[1]
        