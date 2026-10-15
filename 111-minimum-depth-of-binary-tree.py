# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root,count):
    if root.left is None and root.right is None:
        return count
    depth=None
    if root.left:
        result=min_depth(root.left,count+1)
        if depth is None or result<depth:
            depth=result
    if root.right:
        result=min_depth(root.right,count+1)
        if depth is None or result<depth:
            depth=result
    return depth
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        return min_depth(root,1)
    
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
        