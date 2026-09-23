class Solution(object):
    def reverseStr(self, s, k):
        left=0
        right=k-1
        list_string=list(s)
        start=0
        while start<len(s):
            left=start
            right=start+(k-1)
            if right>len(s)-1:
                right=len(s)-1
            while left<right:
                temp=list_string[left]
                list_string[left]=list_string[right]
                list_string[right]=temp
                left+=1
                right-=1
            start+=2*k
        return "".join(list_string)