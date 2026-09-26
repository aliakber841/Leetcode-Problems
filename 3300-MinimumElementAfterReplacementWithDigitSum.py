class Solution(object):
    def minElement(self, nums):
        for i in range(len(nums)):
            remaining_digits=nums[i]
            digitSum=0
            while remaining_digits>0:
                digit=remaining_digits%10
                remaining_digits=remaining_digits//10
                digitSum+=digit
            nums[i]=digitSum
        
        minimum=-1
        for i in range(len(nums)):
            if minimum==-1 or nums[i]<minimum:
                minimum=nums[i]
        return minimum