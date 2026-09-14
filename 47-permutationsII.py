def getPerm(nums,index,result):
    if index==len(nums):
        result.append(nums[:])
        return
    
    seen=set()
    for i in range(index,len(nums)):
        if nums[i] in seen:
            continue
        
        seen.add(nums[i])

        temp=nums[i]
        nums[i]=nums[index]
        nums[index]=temp

        getPerm(nums,index+1,result)

        temp=nums[i]
        nums[i]=nums[index]
        nums[index]=temp
class Solution(object):
    def permuteUnique(self, nums):
        result=[]
        getPerm(nums,0,result)
        return result
        