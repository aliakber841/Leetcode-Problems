def printSubset(nums,result,i,subsets):
    if i==len(nums):
        subsets.append(list(result))
        return
        
    result.append(nums[i])
    printSubset(nums,result,i+1,subsets)

    result.pop()
    printSubset(nums,result,i+1,subsets)

class Solution(object):
    def subsets(self, nums):
        result=[]
        subsets=[]
        printSubset(nums,result,0,subsets)
        return subsets