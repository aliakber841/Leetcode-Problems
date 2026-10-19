class Solution(object):
    def findMin(self, nums):
        # [7,0,1,2,4,5,6]
        left=0
        right=len(nums)-1
        minimum=nums[0]
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]<=minimum:
                minimum=nums[mid]
            if nums[mid]>=nums[left]:
                if nums[left]<=minimum:
                    minimum=nums[left]
                left=mid+1
            elif nums[right]>=nums[mid]:   
                right=mid-1 
        return minimum 