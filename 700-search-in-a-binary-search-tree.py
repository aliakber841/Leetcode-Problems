# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, val):
        def subtree(root,val):
            if not root:
                return None
            elif val==root.val:
                return root
            elif val<root.val:
                return subtree(root.left,val)
            elif val>root.val:
                return subtree(root.right,val)
        return subtree(root,val)
        