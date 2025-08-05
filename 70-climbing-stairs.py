# Two Variables Approach (Optimal)
class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return n
        first=1
        second=2
        for i in range(3,n+1):
            third=first+second
            first=second
            second=third
        return second
# Memoization
class Solution(object):
    def climbStairs(self, n):
        memo={}
        def stairsStep(num):
            if num<0:
                return 0
            if num==0:
                return 1
            if num in memo:
                return memo[num]
            memo[num]=stairsStep(num-1)+stairsStep(num-2)
            return memo[num]
        return stairsStep(n)