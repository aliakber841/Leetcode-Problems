def checkDigit(num,result):
    isValid=True
    digit=num
    while digit>0:
        current_digit=digit%10
        if current_digit==0 or num%current_digit!=0:
            isValid=False
            break
        
        digit=digit//10
    if isValid:
        result.append(num)

class Solution(object):
    def selfDividingNumbers(self, left, right):
        result=[]
        while left<=right:
            checkDigit(left,result)
            left+=1
        return result