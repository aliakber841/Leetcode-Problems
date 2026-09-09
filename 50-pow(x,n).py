class Solution(object):
    def myPow(self, x, n):
        result=1
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        while n>0:
            if n%2==1:
                result*=x
            x*=x
            n=n//2
        return result

#Recursion
class Solution(object):
    def myPow(self, x, n):
        def power(x,n,result):
            if n==0:
                return result
            elif n%2==1:
                result*=x
            x*=x  #2^2=4=> 4*4=16 => 16*16=256
            n=n//2 #5=>2=>1
            # result=1=>4=>256*4=1024
            return power(x,n,result)

        if n<0:
            x=1/x
            n=-n
        result=1
        return power(x,n,result)
    
# class Solution(object):
#     def myPow(self, x, n):
#         return pow(x,n)