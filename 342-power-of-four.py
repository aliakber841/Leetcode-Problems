# Math (Optimal)
class Solution(object):
    def isPowerOfFour(self, n):
        if (n<=0):
            return False
        while (n>1):
            if (n%4!=0):
                return False
            n//=4
        return True

# Recursion ( Best for Runtime and decent for Space)
class Solution(object):
    def isPowerOfFour(self, n):
        if (n<=0):
            return False
        def power(result):
            if (result==n or n==1):
                return True
            if (result>n):
                return False
            result*=4
            return power(result)
        return power(1) 

# Recursion ( Best for Runtime but not for Space)  
class Solution(object):
    def isPowerOfFour(self, n):
        if (n<=0):
            return False
        result=1
        while (result<=n):
            if (result==n):
                return True
            result*=4
        return False