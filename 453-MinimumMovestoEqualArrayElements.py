class Solution(object):
    def minMoves(self, nums):
        minimum=nums[0]
        total=nums[0]
        for i in range(1,len(nums)):
            total+=nums[i]
            if nums[i]<minimum:
                minimum=nums[i]
        return total-minimum*len(nums)  

class Solution(object):
    def minMoves(self, nums):
        minimum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<minimum:
                minimum=nums[i]
        
        total=0
        for i in range(len(nums)):
            total+=nums[i]-minimum
        return total