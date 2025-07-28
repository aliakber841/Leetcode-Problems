# Memoization
class Solution(object):
    def fib(self, n):
        memo={0:0,1:1}
        def cal(n):
            if n not in memo:
                  memo[n]= cal(n-1)+cal(n-2)
            return memo[n]
        return cal(n)

#Tabulation
# class Solution(object):
#     def fib(self, n):
#         if (n==0 or n==1):
#              return n
#         dp=[0]*(n+1)
#         dp[0]=0
#         dp[1]=1
#         for i in range(2,n+1):
#             dp[i]= dp[i-2]+dp[i-1]
#         return dp[n]

# Two variables approach
# class Solution(object):
#     def fib(self, n):
#         if (n==0 or n==1):
#             return n
#         num=1
#         previous=0
#         for i in range(2,n+1):
#             temp=num+previous
#             previous=num
#             num=temp
#         return num

# Simple Recursion
# class Solution(object):
#     def fib(self, n):
#         def cal(n):
#             if (n==0 or n==1):
#              return n
#             return cal(n-2)+cal(n-1)
#         return cal(n)