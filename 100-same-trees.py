# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def compare(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val!=root2.val:
        return False
    elif root1.val==root2.val:
        return compare(root1.left,root2.left) and compare(root1.right,root2.right)
class Solution(object):
    def isSameTree(self, p, q):
       return compare(p,q)
    
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