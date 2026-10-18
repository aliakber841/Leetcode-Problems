class Solution(object):
    def searchRange(self, nums, target):
        left=0
        right=len(nums)-1
        result=[]

        start=-1
        end=-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                start=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1

        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                end=mid
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1

        result.append(start)
        result.append(end)
        return result