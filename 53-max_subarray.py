class Solution(object):
    def maxSubArray(self, nums):
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        max_sum=nums[0]
        current_sum=nums[0]
        if len(nums)>1:
            for i in range(1,len(nums)):
             if current_sum+nums[i]<nums[i]:
                current_sum=nums[i]
             else:
                current_sum+=nums[i]
             if max_sum<current_sum:
                max_sum=current_sum
        return max_sum