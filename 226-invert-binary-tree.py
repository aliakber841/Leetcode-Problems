# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invert_tree(root):
    if not root:
        return None
    left=invert_tree(root.left)  
    right=invert_tree(root.right)

    root.left=right
    root.right=left
    return root
class Solution(object):
    def invertTree(self, root):
        return invert_tree(root)
    
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        def subtree(root):
            if not root:
                return None
            left_subtree=subtree(root.left)
            right_subtree=subtree(root.right)
            root.left=right_subtree
            root.right=left_subtree
            return root
        return subtree(root)  