# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        def subtree(original,cloned,target):
            if not original and not cloned:
                return None
            if original==target:
                return cloned
            left_subtree=subtree(original.left,cloned.left,target)
            right_subtree=subtree(original.right,cloned.right,target)
            if left_subtree or right_subtree:
                return left_subtree or right_subtree
            else:
                return None
        return subtree(original,cloned,target)   