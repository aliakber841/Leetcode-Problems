class Solution(object):
    def sumZero(self, n):
        result=[]
        if n%2==0:
            for i in range(1,n//2+1):
                result.append(i)
                result.append(-i)
        else:
            result.append(0) 
            for i in range(1,n//2+1):
                 result.append(i)
                 result.append(-i)
        return result