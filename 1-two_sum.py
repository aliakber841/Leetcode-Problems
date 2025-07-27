class Solution(object):
    def twoSum(self, nums, target):
        hash_table={}
        for i,num in enumerate(nums):
            remainder=target-nums[i]
            if remainder in hash_table:
                return [hash_table[remainder],i]
            hash_table[num]=i
        return []
