class Solution(object):
    def findMissingElements(self, nums):
        hash_set=set()
        result=[]
        min_num=nums[0]
        max_num=nums[0]
        for i in range(len(nums)):
            hash_set.add(nums[i])
            if nums[i]<min_num:
                min_num=nums[i]
            if nums[i]>max_num:
                max_num=nums[i]
   
        while min_num<=max_num:
            if min_num not in hash_set:
                result.append(min_num)
            min_num+=1
        return result