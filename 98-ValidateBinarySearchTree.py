# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def compare(root,low,high):
    if not root:
        return True
    if low is not None and root.val<=low:
        return False
    if high is not None and root.val>=high:
        return False
    left=compare(root.left,low,root.val)
    right=compare(root.right,root.val,high)
    return right and left
class Solution(object):
    def isValidBST(self, root):
        return compare(root,None,None)