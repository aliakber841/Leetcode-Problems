class Solution(object):
    def getSneakyNumbers(self, nums):
        hash_table={}
        result=[]
        for i in range(len(nums)):
            if nums[i] in hash_table:
                hash_table[nums[i]]+=1
            else:
                hash_table[nums[i]]=1
        for key in hash_table:
            if hash_table[key]>1:
                result.append(key)
        return result