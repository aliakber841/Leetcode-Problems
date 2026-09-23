class Solution(object):
    def generate(self, numRows):
        result=[]
        for i in range(numRows):
            nums=[1]*(i+1)
            for j in range(1,i):
                nums[j]=result[i-1][j-1]+result[i-1][j]
            result.append(nums)
        return result