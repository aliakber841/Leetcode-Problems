class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        i=0
        j=1
        result=[]
        while j<len(nums):
            result.append(nums[j])
            result.append(nums[i])
            i+=2
            j+=2
        return result

class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        i=0
        j=1
        while j<len(nums):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i+=2
            j+=2
        return nums