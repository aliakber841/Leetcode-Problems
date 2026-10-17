# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root,best):
    if not root:
        return 0
    left=0
    right=0
    if root.left:
        left=height(root.left,best)
    if root.right:
        right=height(root.right,best)
    if left+right>best[0]:
        best[0]=left+right
    if left==right:
        return left+1
    elif left>right:
        return left+1
    else:
        return right+1
class Solution(object):
    def diameterOfBinaryTree(self, root):
        best=[0]
        height(root,best)   
        return best[0]  