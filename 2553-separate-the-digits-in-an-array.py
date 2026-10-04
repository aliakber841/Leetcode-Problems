class Solution(object):
    def separateDigits(self, nums):
        result=[]
        for i in range(len(nums)):
            digit_list=[]
            current=nums[i]
            digit=current
            remaining_digits=digit
            while remaining_digits>0:
                digit=remaining_digits%10
                remaining_digits=remaining_digits//10
                digit_list.append(digit)
            for i in range(len(digit_list)-1,-1,-1):
                result.append(digit_list[i])
        return result      