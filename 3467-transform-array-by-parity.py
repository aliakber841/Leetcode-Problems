class Solution(object):
    def transformArray(self, nums):
        count_zero=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
                count_zero+=1
            elif nums[i]%2!=0:
                nums[i]=1
        for j in range(len(nums)):
            if j<count_zero:
                nums[j]=0
            else:
                nums[j]=1
        return nums