class Solution(object):
    def sumOfUnique(self, nums):
        hash_table={}
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]]=1
            else:
                hash_table[nums[i]]+=1
        
        unique_sum=0
        for i in range(len(nums)):
            if hash_table[nums[i]]==1:
                unique_sum+=nums[i]
        return unique_sum  