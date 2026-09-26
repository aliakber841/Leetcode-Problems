class Solution(object):
    def mirrorDistance(self, n):
        remaining_digit=n
        reverse_digit=0
        while remaining_digit>0:
            digit=remaining_digit%10
            reverse_digit= reverse_digit*10+digit
            remaining_digit=remaining_digit//10
        
        return abs(n-reverse_digit)
    
class Solution(object):
    def mirrorDistance(self, n):
        digit=n
        remaining_digit=digit
        reverse_digit=""
        while remaining_digit>0:
            digit=remaining_digit%10
            remaining_digit=remaining_digit//10
            reverse_digit+=str(digit)
        
        reverse=int(reverse_digit)
        return abs(n-reverse)
        