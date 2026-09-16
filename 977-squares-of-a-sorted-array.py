class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        left=0
        right=n-1
        result=[0]*n
        index=n-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[index]=nums[left]*nums[left]
                left+=1
            else:
                result[index]=nums[right]*nums[right]
                right-=1
            index-=1
        
        return result 