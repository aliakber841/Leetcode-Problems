class Solution(object):
    def sumCounts(self, nums):
        result=0
        for i in range(len(nums)):
            seen=set()
            for j in range(i,len(nums)):
                seen.add(nums[j])            
                count=len(seen)            
                result+=count*count  
        return result     