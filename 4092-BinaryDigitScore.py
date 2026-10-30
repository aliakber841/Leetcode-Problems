class Solution(object):
    def calculateScore(self, a, b):
        s1=bin(a).count('1')
        s2=bin(b).count('1')
        if s1>=s2:
            return s1*s2
        else:
            return s2//s1

class Solution(object):
    def calculateScore(self, a, b):
        s1=0
        s2=0
        while a>0:
            s1+=a%2
            a//=2

        while b>0:
            s2+=b%2
            b//=2

        if s1>=s2:
            return s1*s2

        return s2//s1  