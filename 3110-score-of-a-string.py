class Solution(object):
    def scoreOfString(self, s):
        result=0
        for i in range(len(s)):
            ascii_value=ord(s[i])
            if i+1<len(s):
                next_value=ord(s[i+1])
                diff=abs(ascii_value-next_value)
                result+=diff
        return result