# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_nodes(root,low,high):
    if not root:
        return 0
    if root.val<low:
        return sum_nodes(root.right,low,high)
    if root.val>high:
        return sum_nodes(root.left,low,high)
    current_sum=root.val
    left=sum_nodes(root.left,low,high)
    right=sum_nodes(root.right,low,high)
    return left+right+current_sum
class Solution(object):
    def rangeSumBST(self, root, low, high):
       result=0
       return sum_nodes(root,low,high)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_nodes(root,low,high):
    if not root:
        return 0
    current_sum=0
    if root.val>=low and root.val<=high:
        current_sum+=root.val
    left=sum_nodes(root.left,low,high)
    right=sum_nodes(root.right,low,high)
    return left+right+current_sum
class Solution(object):
    def rangeSumBST(self, root, low, high):
       result=0
       return sum_nodes(root,low,high)
    
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        def subtree(root,low,high):
            if not root:
                return 0
            current_sum=0
            if root.val>=low and root.val<=high:
                current_sum+=root.val
            left_subtree=subtree(root.left,low,high)
            right_subtree=subtree(root.right,low,high)
            return current_sum+left_subtree+right_subtree
        return subtree(root,low,high)  