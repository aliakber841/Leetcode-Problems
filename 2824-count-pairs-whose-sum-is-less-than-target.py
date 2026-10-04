class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        count=0
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]+nums[right]<target:
                pairs=right-left # means pairs from left to right will also be valid 
                count+=pairs
                left+=1
            else:
                right-=1
        return count    

class Solution(object):
    def countPairs(self, nums, target):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    count+=1
        return count    