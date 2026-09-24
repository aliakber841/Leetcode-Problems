class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        sum_digits=0
        count=0
        for i in range(len(nums)):
           sum_digits+=nums[i]
           while sum_digits>=target:
            window_length=i-left+1
            if count==0:
                count=window_length
            elif window_length<count:
                count=window_length
            sum_digits-=nums[left]
            left+=1
        return count