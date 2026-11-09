def calculatePrime(num):
    x=2
    while x*x<=num:
        if num%x==0:
            return x
        x+=1
    return num
class Solution(object):
    def minimumMaxValue(self, n, index, value):
        if value<2:
            return -1
        if n==1:
            return value

        prime=calculatePrime(value)
        if index>0:
            if value%2==0:
                low=value-2*index
            else:
                if prime==value:
                    return -1
                low=value-prime-2*(index-1)
            if low<2:
                return -1

        current=n-1-index
        if current==0:
            return value
        if value%2==0:
            return value+2*current
            
        return value+prime+2*(current-1)