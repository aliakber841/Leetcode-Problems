class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n=len(nums)
        min_sum=-1
        for length in range(l,r+1):
            for left in range(0,n-length+1):
                sub_sum=0
                for i in range(left,left+length):
                    sub_sum+=nums[i]
                if sub_sum>0:
                    if min_sum==-1:
                        min_sum=sub_sum
                    elif sub_sum<min_sum:
                        min_sum=sub_sum
        return min_sum

class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n=len(nums)
        sum_digits=[0]*(n+1)
        min_sum=-1
        for i in range(n):
            sum_digits[i+1]=sum_digits[i]+nums[i]
            for length in range(l,r+1):
                left=i-length+1
                if left>=0:
                    sub_sum=sum_digits[i+1]-sum_digits[left]
                    if sub_sum>0:
                        if min_sum==-1:
                            min_sum=sub_sum
                        elif sub_sum<min_sum:
                            min_sum=sub_sum
        return min_sum