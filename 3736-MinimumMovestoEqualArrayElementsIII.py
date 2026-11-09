class Solution(object):
    def minMoves(self, nums):
        maximum=0
        for i in range(len(nums)):
            if nums[i]>maximum:
                maximum=nums[i]
        
        count=0
        for i in range(len(nums)):
            while nums[i]<maximum:
                nums[i]=nums[i]+1
                count+=1
        return count