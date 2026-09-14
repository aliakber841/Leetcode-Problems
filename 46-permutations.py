def getPerm(nums,index,result):
    if index==len(nums):
        result.append(nums[:])
    for i in range(index,len(nums)):
        temp=nums[i]
        nums[i]=nums[index]
        nums[index]=temp

        getPerm(nums,index+1,result)

        temp=nums[i]
        nums[i]=nums[index]
        nums[index]=temp
class Solution(object):
    def permute(self, nums):
       result=[]
       getPerm(nums,0,result)
       return result