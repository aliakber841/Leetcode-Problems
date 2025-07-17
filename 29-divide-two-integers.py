class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX=2**31-1
        INT_MIN=-2**31
        if (dividend==INT_MIN and divisor==-1):
            return INT_MAX
        negative=(dividend<0)!=(divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        quotient=0
        while dividend>=divisor:
            temp_divisor=divisor
            temp_quotient=1
            while dividend>=(temp_divisor+temp_divisor):
                temp_divisor+=temp_divisor
                temp_quotient+=temp_quotient
            dividend-=temp_divisor
            quotient+=temp_quotient
        if negative:
            quotient=-quotient
        return max(min(quotient,INT_MAX),INT_MIN)