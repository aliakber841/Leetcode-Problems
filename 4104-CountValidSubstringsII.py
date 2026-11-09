class Solution(object):
    def countValidSubstrings(self, s):
        score=0
        a=-1
        b=-1
        c=-1
        for i in range(len(s)):
            current=s[i]
            if current=="a":
                a=i
            if current=="b":
                b=a
            if current=="c":
                c=b

            startFrom=i-c
            score+=startFrom

        return score 