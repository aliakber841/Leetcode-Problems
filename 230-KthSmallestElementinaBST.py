# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def smallest(root,result,k):
    if not root:
        return
    if len(result)==k:
        return
    smallest(root.left,result,k)
    if len(result)==k:
        return
    result.append(root.val)
    smallest(root.right,result,k)

class Solution(object):
    def kthSmallest(self, root, k):
        result=[]
        smallest(root,result,k)
        return result[k-1]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def smallest(root,result):
    if not root:
        return None
    if root.left:
        left=smallest(root.left,result)
    result.append(root.val)
    if root.right:
        right=smallest(root.right,result)
class Solution(object):
    def kthSmallest(self, root, k):
        result=[]
        smallest(root,result)
        return result[k-1]
        
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
def smallest(root,result):
    if not root:
        return None
    if root.left:
        left=smallest(root.left,result)
    result.append(root.val)
    if root.right:
        right=smallest(root.right,result)
class Solution(object):
    def kthSmallest(self, root, k):
        result=[]
        smallest(root,result)
        if k>len(result):
            return -1
        heap=[]
        for i in range(len(result)):
            heapq.heappush(heap,result[i])
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)
        