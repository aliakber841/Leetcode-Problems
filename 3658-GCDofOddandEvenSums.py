class Solution(object):
    def gcdOfOddEvenSums(self, n):
        odd=1
        even=2
        num=3
        while n>1:
            odd+=num
            even+=num+1
            num+=2
            n-=1

        while odd>0:
            remainder=even%odd
            even=odd
            odd=remainder 
        return even