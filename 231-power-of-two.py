# Math ( Best for Memory)
class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        while n>1:
            if (n%2!=0):
                return False
            n//=2
        return True

# Loop ( Best for Runtime)
class Solution(object):
    def isPowerOfTwo(self, n):
        result=1
        while result<=n:
            if (result==n):
                return True
            result*=2
        return False
    
# Recursion ( Not Good for Both Runtimes)
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         def power(result):
#             if(result==n or n==1):
#                 return True
#             if (result>n):
#                 return False
#             result*=2
#             return power(result)
#         return power(1)