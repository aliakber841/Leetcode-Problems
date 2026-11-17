class Solution(object):
    def digitSum(self, s, k):
        while len(s)>k:
            result=""
            current=""
            for i in range(len(s)):
                current+=s[i]
                if len(current)==k or i==len(s)-1:
                    value=int(current)
                    remaining_digits=value
                    sumDigits=0
                    while remaining_digits>0:
                        digit=remaining_digits%10
                        remaining_digits=remaining_digits//10
                        sumDigits+=digit
                    result+=str(sumDigits)
                    current=""
            s=result

        return s 