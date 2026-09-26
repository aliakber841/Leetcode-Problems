class Solution(object):
    def differenceOfSum(self, nums):
        element_sum=0
        digit_sum=0
        for i in range(len(nums)):
            element_sum+=nums[i]
            remaining_digits=nums[i]
            while remaining_digits>0:
                digit=remaining_digits%10
                digit_sum+=digit
                remaining_digits=remaining_digits//10
        return abs(element_sum-digit_sum)
    
class Solution(object):
    def differenceOfSum(self, nums):
        element_sum=0
        digit_sum=0
        for i in range(len(nums)):
            element_sum+=nums[i]
            current_length=str(nums[i])

            remaining_digits=nums[i]
            if current_length>1:
                while remaining_digits>0:
                    digit=remaining_digits%10
                    digit_sum+=digit
                    remaining_digits=remaining_digits//10
            else:
                digit_sum+=nums[i]
        
        return abs(element_sum-digit_sum)