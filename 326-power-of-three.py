# Math ( Better for Both )
class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        while n>1:
            if (n%3!=0):
                return False
            n//=3
        return True

# Loop
class Solution(object):
    def isPowerOfThree(self, n):
        if (n<=0):
            return False
        result=1
        while (result<=n):
            if (result==n):
                return True
            result*=3
        return False

# Recursion ( Not Good for Both Runtimes)
# class Solution(object):
#     def isPowerOfThree(self, n):
#         if (n<=0):
#             return False
#         def power(result):
#             if (result==n or n==1):
#                 return True
#             if (result>n):
#                 return False
#             result*=3
#             return power(result)
#         return power(1)      