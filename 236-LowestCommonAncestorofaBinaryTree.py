# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def findAncestor(root,p,q):
    if not root:
        return None
    if root==p or root==q:
        return root
    left=findAncestor(root.left,p,q)
    right=findAncestor(root.right,p,q)
    if left and right:
        return root
    if left:
        return left
    return right
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return findAncestor(root,p,q)