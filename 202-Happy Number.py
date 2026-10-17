def findDigits(remaining_digits,result):
    while remaining_digits>0:
        digit=remaining_digits%10
        remaining_digits=remaining_digits//10
        result+=digit*digit
    return result
class Solution(object):
    def isHappy(self, n):
        seen=set()
        remaining_digits=n
        result=0
        number=findDigits(remaining_digits,result)
        
        while number!=1:
            if number in seen:
                return False
            seen.add(number)
            number=findDigits(number,result) 
        return True   