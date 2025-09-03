class Solution(object):
    def buildArray(self, nums):
        result=[0]*len(nums)
        for i in range(len(nums)):
            result[i]=nums[nums[i]]
        return result