class Solution(object):
    def findDisappearedNumbers(self, nums):
        hash_table=set() 
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table.add(nums[i])
       
        result=[]
        for i in range(1,len(nums)+1):
            if i not in hash_table:
                result.append(i)
        return result

class Solution(object):
    def findDisappearedNumbers(self, nums):
        hash_table=set(nums) 
        result=[]
        for i in range(1,len(nums)+1):
            if i not in hash_table:
                result.append(i)
        return result