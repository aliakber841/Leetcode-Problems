# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        def subtree(root,is_left):
            if not root:
                return 0
            if not root.left and not root.right:
                if is_left:
                    return root.val
                else:
                     return 0
            left_subtree=subtree(root.left,True)
            right_subtree=subtree(root.right,False)
            return left_subtree+right_subtree
        return subtree(root,False)