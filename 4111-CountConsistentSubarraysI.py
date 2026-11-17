class Solution(object):
    def countConsistent(self, nums):
        n=len(nums)
        result=0
        for i in range(n):
            currentAnd=nums[i]
            currentMin=nums[i]
            for j in range(i,n):
                currentAnd=currentAnd & nums[j]
                if nums[j]<currentMin:
                    currentMin=nums[j]
                if currentMin==currentAnd:
                    result+=1
        return result