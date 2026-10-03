class Solution(object):
    def missingNumber(self, nums):
        hash_set=set()
        for i in range(len(nums)):
            hash_set.add(nums[i])

        n=len(nums)
        
        while n>=0:
            if n not in hash_set:
                return n
            n-=1