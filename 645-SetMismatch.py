class Solution(object):
    def findErrorNums(self, nums):
        hash_table={}
        duplicate=0
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]]=1
            else:
                duplicate=nums[i]
        
        for i in range(1,len(nums)+1):
            if i not in hash_table:
                return [duplicate,i]