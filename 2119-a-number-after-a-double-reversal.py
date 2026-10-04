def reverse_number(number):
    reversed_number=0
    remaining_digits=number
    while remaining_digits>0:
        digit=remaining_digits%10
        remaining_digits=remaining_digits//10

        reversed_number=reversed_number*10
        reversed_number=reversed_number+digit
    return reversed_number
class Solution(object):
    def isSameAfterReversals(self, num):
        reversed1=reverse_number(num)
        reversed2=reverse_number(reversed1)
        if reversed2==num:
            return True
        else:
            return False