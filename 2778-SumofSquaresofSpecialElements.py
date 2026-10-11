class Solution(object):
    def sumOfSquares(self, nums):
        n=len(nums)
        result=0
        for i in range(len(nums)+1):
            if n%(i+1)==0:
                result+=nums[i]*nums[i]
        return result     