class Solution(object):
    def maxProduct(self, nums):
        result=[]
        product=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if product<(nums[i]-1)*(nums[j]-1):
                    product=(nums[i]-1)*(nums[j]-1)
        return product

class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        n=len(nums)
        return (nums[n-1]-1)*(nums[n-2]-1)