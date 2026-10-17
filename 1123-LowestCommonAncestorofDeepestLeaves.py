# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth(root,count):
    if not root:
        return None
    count+=1
    left_root=root
    left_depth=count
    right_root=root
    right_depth=count
    if not root.left and not root.right:
        return root,count
    if root.left:
        left_root,left_depth=depth(root.left,count)
    if root.right:
        right_root,right_depth=depth(root.right,count)
    if left_depth==right_depth:
        return root,left_depth
    if left_depth>right_depth:
        return left_root,left_depth
    else:
        return right_root,right_depth
class Solution(object):
    def lcaDeepestLeaves(self, root):
        leaf_root,max_depth=depth(root,0)
        return leaf_root