class Solution(object):
    def majorityElement(self, nums):
        hash_table={}
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]]=1
            else:
                hash_table[nums[i]]+=1
        
        for key in hash_table:
            if hash_table[key]>(len(nums))//2:
                return key 