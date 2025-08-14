# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def compareTrees(p,q):
             if not p and not q:
                return True
             if not p or not q:
                return False
             if p.val!=q.val:
                 return False
             return compareTrees(p.left,q.left) and compareTrees(p.right,q.right)
        return compareTrees(p,q)