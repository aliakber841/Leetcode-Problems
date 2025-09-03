class Solution(object):
    def numIdenticalPairs(self, nums):
        count_pairs=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]==nums[i] and i<j:
                    count_pairs+=1
        return count_pairs