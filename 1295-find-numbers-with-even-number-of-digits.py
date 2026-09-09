class Solution(object):
    def findNumbers(self, nums):
        count=0
        for i in range(len(nums)):
            digit_count=0
            digit=nums[i] 
            remaining_digits=digit
            while remaining_digits>0:
                digit=i%10
                remaining_digits=remaining_digits//10
                digit_count+=1
            if digit_count%2==0:
                count+=1
        return count