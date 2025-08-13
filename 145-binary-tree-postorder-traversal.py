# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result=[]
        def buildTree(root):
            if not root:
                return
            buildTree(root.left)
            buildTree(root.right)
            result.append(root.val)
        buildTree(root)
        return result