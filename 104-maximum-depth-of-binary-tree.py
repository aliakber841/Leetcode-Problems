# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root,count):
    depth=count
    if root.left:
        result=height(root.left,count+1)
        if depth<result:
            depth=result
    if root.right:
        result=height(root.right,count+1) 
        if depth<result:
            depth=result
    return depth
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return height(root,1)
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root,count,depth):
    if not root:
        return depth
    left=count
    right=count
    if root.left:
        left=height(root.left,count+1,depth)
    if root.right:
        right=height(root.right,count+1,depth) 
    depth=left
    if depth<right:
        depth=right
    return depth
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return height(root,1,1)
    
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        def subtree(root):
            if not root:
                return 0
            left_subtree=subtree(root.left)+1
            right_subtree=subtree(root.right)+1
            return max(left_subtree,right_subtree)
        return subtree(root)