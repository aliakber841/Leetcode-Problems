class Solution(object):
    def maxDifference(self, nums):
        n=len(nums)
        result=[]
        for i in range(n+1):
            result.append([0,0])

        for i in range(n-1,-1,-1):
            bestTurn=None
            current=nums[i]
            if current%3==0:
                nextTurn=1
            else:
                nextTurn=0

            choice=current+result[i+1][nextTurn]
            bestTurn=choice

            if i+1<n:
                current=nums[i]+nums[i+1]
                if current%3==0:
                    nextTurn=1
                else:
                    nextTurn=0
                choice=current+result[i+2][nextTurn]
                if choice>bestTurn:
                    bestTurn=choice

            result[i][0]=bestTurn

            #Bob
            bestTurn=None
            current=nums[i]
            if current%3==0:
                nextTurn=0
            else:
                nextTurn=1
            choice=-current+result[i+1][nextTurn]
            bestTurn=choice

            if i+1<n:
                current=nums[i]+nums[i+1]
                if current%3==0:
                    nextTurn=0
                else:
                    nextTurn=1
                choice=-current+result[i+2][nextTurn]
                if choice<bestTurn:
                    bestTurn=choice

            result[i][1]=bestTurn

        return result[0][0]