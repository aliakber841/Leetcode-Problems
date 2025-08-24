# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        result=[]
        def subtree(root,path):
            if not root:
                return None
            path+=str(root.val)
            if not root.left and not root.right:
                result.append(path)
            else:
                path+="->"
            subtree(root.left,path)
            subtree(root.right,path)
        subtree(root,"")
        return result