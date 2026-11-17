class Solution(object):
    def longestMonotonicSubarray(self, nums):
        increase=1
        decrease=1
        num=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]>num:
                count+=1
                num=nums[i]
                if increase<count:
                    increase=count
                if i+1<len(nums):
                    if nums[i+1]<num:
                        count=1
            elif nums[i]<num:
                count+=1
                num=nums[i]
                if decrease<count:
                    decrease=count
                if i+1<len(nums):
                    if nums[i+1]>num:
                        count=1
            else:
                count=1
        return max(increase,decrease)