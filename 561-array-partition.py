class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        maximum=0
        for i in range(0,len(nums),2):
            maximum+=nums[i]
        return maximum