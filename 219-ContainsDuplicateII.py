class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hash_table={}
        for i in range(len(nums)):
            if nums[i] in hash_table and i-hash_table[nums[i]]<=k:
                return True
            else:
                hash_table[nums[i]]=i
        return False