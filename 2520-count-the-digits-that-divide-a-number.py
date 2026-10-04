class Solution(object):
    def countDigits(self, num):
        count=0
        digit=num
        remaining_digits=digit
        if num<=9:
            return 1
        elif num>=10:
            while remaining_digits>0:
                digit=remaining_digits%10
                remaining_digits=remaining_digits//10
                if digit==1:
                    count+=1
                elif digit>0 and num%digit==0:
                    count+=1
        return count