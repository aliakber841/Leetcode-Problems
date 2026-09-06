# XOR Approach
class Solution(object):
    def singleNumber(self, nums):
        result=0
        for i in range(len(nums)):
            result=nums[i]^result
        return result

# Hash Table Approach
class Solution(object):
    def singleNumber(self, nums):
        hash_table={}
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]]=1
            elif nums[i] in hash_table:
                hash_table[nums[i]]+=1
        
        for key,value in hash_table.items():
            if value==1:
                return key