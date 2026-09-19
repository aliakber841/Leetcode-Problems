class Solution(object):
    def pivotIndex(self, nums):
        prefixSum=0
        leftSum=0
        for i in range(0,len(nums)):
            prefixSum+=nums[i]
        
        for j in range(0,len(nums)):
            rightSum=prefixSum-leftSum-nums[j]
            if leftSum==rightSum:
                return j
            leftSum+=nums[j]
        return -1