class Solution(object):
    def smallestIndex(self, nums):
        for i in range(0,len(nums)):
            if nums[i]<=9:
                if nums[i]==i:
                    return i
            elif nums[i]>=10:
                digit=nums[i]
                remaining_digits=digit
                sum_digits=0
                while remaining_digits>0:
                    digit=remaining_digits%10
                    sum_digits+=digit
                    remaining_digits=remaining_digits//10
                if sum_digits==i:
                    return i
        return -1      