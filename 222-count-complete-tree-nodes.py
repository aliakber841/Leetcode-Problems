# Optimal O log n
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countNodes(self, root):
        def height(root):
            h=0
            while root:
                h+=1
                root=root.left
            return h
        if not root:
            return 0
        left_height=height(root.left)
        right_height=height(root.right)
        if left_height==right_height:
            return pow(2,left_height)+self.countNodes(root.right)
        else:
            return pow(2,right_height)+self.countNodes(root.left)



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countNodes(self, root):
        def subtree(root):
            if not root:
                return 0
            return 1+subtree(root.left)+subtree(root.right)
        return subtree(root)
        