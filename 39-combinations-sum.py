def getComb(candidates,i,nums,result,target,seen):
    if target<0 or i==len(candidates):
        return 

    if target==0:
        key=tuple(sorted(nums))
        if key not in seen:
            seen.add(key)
            result.append(list(nums))
        return

    nums.append(candidates[i])
    getComb(candidates,i+1,nums,result,target-candidates[i],seen) #single num
    getComb(candidates,i,nums,result,target-candidates[i],seen) #num multiple times
    nums.pop() #backtrack
    getComb(candidates,i+1,nums,result,target,seen) #excluded element

class Solution(object):
    def combinationSum(self, candidates, target):
        nums=[]
        result=[]
        seen=set()
        getComb(candidates,0,nums,result,target,seen)
        return result


#2nd Approach
def getComb(candidates,i,nums,result,target):
    if target<0 or i==len(candidates):
        return 

    if target==0:
        result.append(list(nums))
        return

    nums.append(candidates[i])
    getComb(candidates,i,nums,result,target-candidates[i]) #single num
    nums.pop() #backtrack
    getComb(candidates,i+1,nums,result,target) 

class Solution(object):
    def combinationSum(self, candidates, target):
        nums=[]
        result=[]
        getComb(candidates,0,nums,result,target)
        return result