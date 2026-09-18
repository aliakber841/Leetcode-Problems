def getComb(j,nums,result,n,k):
    if len(nums)==k:
        result.append(list(nums))
        return
    
    for j in range(j,n+1):
        nums.append(j)
        getComb(j+1,nums,result,n,k)
        nums.pop()

class Solution(object):
    def combine(self, n, k):
        nums=[]
        result=[]
        getComb(1,nums,result,n,k)
        return result