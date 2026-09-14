class Solution(object):
    def nextPermutation(self, nums):
        n=len(nums)
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j=n-1
            while nums[j]<=nums[i]:
                j-=1
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        left=i+1
        right=n-1
        while left<=right:
            temp=nums[left]
            nums[left]=nums[right]
            nums[right]=temp
            left+=1
            right-=1