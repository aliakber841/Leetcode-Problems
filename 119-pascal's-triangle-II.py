class Solution(object):
    def getRow(self, rowIndex):
        result=[]
        for i in range(0,rowIndex+1):
            nums=[1]*(i+1)
            for j in range(1,i):
                nums[j]=result[i-1][j-1]+result[i-1][j]
            result.append(nums)
        return result[rowIndex] 