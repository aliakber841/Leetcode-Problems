# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def calculate(root,isFalse):
    if not root:
            return 0
            
    if root.left is None and root.right is None:
        if isFalse:
            return root.val
        else:
            return 0
    left=calculate(root.left,True)
    right=calculate(root.right,False)
    return left+right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        return calculate(root,False)
        
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