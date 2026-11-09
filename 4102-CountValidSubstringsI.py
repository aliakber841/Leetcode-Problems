class Solution(object):
    def countValidSubstrings(self, s):
        score=0
        startFrom=-1
        for i in range(len(s)):
            isValid=False
            if i>=2:
                a=s[i-2]
                b=s[i-1]
                c=s[i]
                if a=="a" and b=="b" and c=="c":
                    isValid=True
    
            if isValid==True:
                startFrom=i-2

            startingIndex=i-startFrom
            score+=startingIndex
            
        return score