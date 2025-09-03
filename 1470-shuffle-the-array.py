class Solution(object):
    def shuffle(self, nums, n):
        result=[]
        for i in range(len(nums)-n):
            result.append(nums[i])
            result.append(nums[n])
            n+=1
        return result