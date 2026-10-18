# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def del_val(root,key):
    if not root:
        return None
    if root.val==key and not root.left and not root.right:
        return None
    if root.val==key and not root.left:
        return root.right
    if root.val==key and not root.right:
        return root.left
    if root.val==key and root.left and root.right:
        current=root.right
        while current.left:
            current=current.left
        current.left=root.left
        return root.right
    if root.val>key:
        root.left=del_val(root.left,key)
    elif root.val<key:
        root.right=del_val(root.right,key)
    return root
class Solution(object):
    def deleteNode(self, root, key):
        return del_val(root,key)   