# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def compare(root,target,skip):
    if not root:
        return False
    if root.val==target:
        return root is not skip
    
    if target>root.val:
        return compare(root.right,target,skip)
    else:
        return compare(root.left,target,skip)

def check_each(root,current,k):
    if not current:
        return False
    partner=k-current.val
    if compare(root,partner,current):
        return True
    
    return check_each(root,current.left,k) or check_each(root,current.right,k)
class Solution(object):
    def findTarget(self, root, k):
        hash_table={}
        return check_each(root,root,k)
    
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
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def compare(root,k,hash_table):
    if not root:
        return False
    remaining=k-root.val
    if root.val in hash_table:
        return True
    else:
        hash_table[remaining]=root    
    return compare(root.left,k,hash_table) or compare(root.right,k,hash_table)
class Solution(object):
    def findTarget(self, root, k):
        hash_table={}
        return compare(root,k,hash_table)
        
        