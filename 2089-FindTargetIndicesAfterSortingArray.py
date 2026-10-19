class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        result=[]
        left=0
        right=len(nums)-1

        start=-1
        end=-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                start=mid
                right=mid-1
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                end=mid
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1

        if start==-1:
            return []

        while start<=end:
            result.append(start)
            start+=1

        return result

class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
        return result
        