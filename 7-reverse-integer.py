class Solution(object):
    def reverse(self, x):
        isNegative=False
        result=0
        if x<0:
            isNegative=True
        digit=abs(x)
        remaining_digits=digit
        while remaining_digits>0:
            digit=remaining_digits%10
            remaining_digits=remaining_digits//10
            result=result*10 
            result=result+digit
        if isNegative:
            result=-result
        if result<-2**31 or result>2**31-1:
            return 0  
        return result