# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bst(root,p,q):
    if not root:
        return None
    if p.val<root.val and q.val<root.val:
        return bst(root.left,p,q)
    if p.val>root.val and q.val>root.val:
        return bst(root.right,p,q)
    
    return root
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return bst(root,p,q) 
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bst(root,p,q):
    if not root:
        return None
    if root==p or root==q:
        return root
    left=bst(root.left,p,q)
    right=bst(root.right,p,q)
    if left and right:
        return root
    if left:
        return left
    return right
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return bst(root,p,q) 
    