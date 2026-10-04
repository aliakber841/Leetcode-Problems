class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        string=list(s)
        left=0
        right=len(string)-1
        while left<right:
            if string[left].isalnum()==False:
                left+=1
                continue
            if string[right].isalnum()==False:
                right-=1 
                continue
            if string[left]!=string[right]:
                return False
            left+=1
            right-=1
        return True