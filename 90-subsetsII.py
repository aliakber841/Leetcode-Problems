def printsubsets(nums,result,subsets,i):
    if i==len(nums):
        subsets.append(list(result))
        return

    result.append(nums[i])
    printsubsets(nums,result,subsets,i+1)
    
    result.pop()
    index=i+1
    while index<len(nums) and nums[index]==nums[index-1]:
        index+=1
    printsubsets(nums,result,subsets,index)

class Solution(object):
    def subsetsWithDup(self, nums):
        result=[]
        subsets=[]
        nums.sort()
        printsubsets(nums,result,subsets,0)
        return subsets