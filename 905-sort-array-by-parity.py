class Solution(object):
    def sortArrayByParity(self, nums):
        left=0
        right=len(nums)-1
        while left<=right:     
            if nums[left]%2==0:
                left+=1
            elif nums[right]%2!=0:
                right-=1
            else:
                temp=nums[right]
                nums[right]=nums[left]
                nums[left]=temp
                right-=1
        return nums

class Solution(object):
    def sortArrayByParity(self, nums):
        odd=[]
        even=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        return even+odd