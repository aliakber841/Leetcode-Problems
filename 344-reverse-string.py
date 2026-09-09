class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while (left<=right):
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
        return s

#Recursion
class Solution(object):
    def reverseString(self, s):
        def reverse(s,left,right):
            if left>=right:
                return
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            return reverse(s,left+1,right-1)
        return reverse(s,0,len(s)-1)