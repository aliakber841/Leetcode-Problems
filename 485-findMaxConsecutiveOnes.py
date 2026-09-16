class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max=0
        current=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                current+=1
                if max<current:
                    max=current 
            elif nums[i]!=1:
                current=0
        return max