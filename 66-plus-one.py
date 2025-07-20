class Solution(object):
    def plusOne(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        digits[0]=1
        digits.append(0)
        return digits