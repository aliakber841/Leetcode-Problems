class Solution(object):
    def decompressRLElist(self, nums):
        result=[]
        for i in range(0,len(nums),2):
            if i+1<len(nums):
                freq=nums[i]
                while freq>0:
                    result.append(nums[i+1])
                    freq-=1
        return result  