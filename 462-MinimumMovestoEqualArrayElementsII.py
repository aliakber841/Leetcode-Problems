class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        median=nums[len(nums)//2]
        total=0
        for i in range(len(nums)):
            total+=abs(median-nums[i])
        return total