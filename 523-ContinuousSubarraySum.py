class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefixSum=0
        hash_table={0:-1}
        #[23,25,29,35,42] PrefixSum
        for i in range(len(nums)):
            prefixSum+=nums[i]
            remainder=prefixSum%k
            if remainder in hash_table:
                if i-hash_table[remainder]>=2:
                    return True
            else:
                hash_table[remainder]=i
        return False     