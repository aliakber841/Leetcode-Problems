# Two Pointers
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findTarget(self, root, k):
        sorted_array=[]
        def subtree(root):
            if not root:
                return None
            subtree(root.left)
            sorted_array.append(root.val)
            subtree(root.right)
        subtree(root)
        left,right=0,len(sorted_array)-1
        while left<right:
            total=sorted_array[left]+sorted_array[right]
            if total==k:
                return True
            elif total<k:
                left+=1
            else:
                right-=1
        return False
    
# Hash Table
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findTarget(self, root, k):
        hash_table={}
        def subtree(root,k):
            if not root:
                return None
            remaining=k-root.val
            if remaining in hash_table:
                return True
            else:
                hash_table[root.val]=True
            left_subtree=subtree(root.left,k)
            right_subtree=subtree(root.right,k)
            if left_subtree or right_subtree:
                return True
            else:
                return False
        return subtree(root,k)
        
        