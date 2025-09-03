class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        hash_table={}
        result=[]
        for i in range(len(nums)):
            if nums[i] in hash_table:
                hash_table[nums[i]]+=1
            else:
                hash_table[nums[i]]=1
        for j in range(len(nums)):
            count=0
            for k in hash_table:
                if nums[j]>k:
                    count+=hash_table[k]
            result.append(count)
        return result     