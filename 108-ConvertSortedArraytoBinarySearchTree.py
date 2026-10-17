# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def build(nums,left,right):
    if left>right:
        return None
    half_length=(left+right)//2
    mid=nums[half_length]
    pivot=TreeNode(val=mid)
    pivot.left=build(nums,left,half_length-1)
    pivot.right=build(nums,half_length+1,right)
    return pivot
class Solution(object):
    def sortedArrayToBST(self, nums):
        return build(nums,0,len(nums)-1)     