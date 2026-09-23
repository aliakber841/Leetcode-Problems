class Solution(object):
    def dominantIndex(self, nums):
        hash_table={}
        maxNumber=0
        for i in range(len(nums)):
            hash_table[nums[i]]=i
            if nums[i]>maxNumber:
                maxNumber=nums[i]
        
        for num in nums:
            if num!=maxNumber and num*2>maxNumber:
                return -1
        return hash_table[maxNumber]