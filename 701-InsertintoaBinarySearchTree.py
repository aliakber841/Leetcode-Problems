# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def insert_val(root,val):
    if not root:
        return None
    if not root.left and val<root.val:
        newNode=TreeNode(val=val)
        root.left=newNode
        return
    if not root.right and val>root.val:
        newNode=TreeNode(val=val)
        root.right=newNode
        return
    if val<root.val:
        insert_val(root.left,val)
    elif val>root.val:
        insert_val(root.right,val)
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val=val)
        insert_val(root,val)
        return root