class Solution(object):
    def findMiddleIndex(self, nums):
        prefixSum=0
        leftSum=0
        for i in range(len(nums)):
            prefixSum+=nums[i]
        
        for j in range(len(nums)):
            rightSum=prefixSum-leftSum-nums[j]
            if leftSum==rightSum:
                return j
            leftSum+=nums[j]
        return -1