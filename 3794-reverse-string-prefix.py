class Solution(object):
    def reversePrefix(self, s, k):
        list_string=list(s)
        left=0
        right=k-1
        while left<right:
            temp=list_string[left]
            list_string[left]=list_string[right]
            list_string[right]=temp

            left+=1
            right-=1
        return "".join(list_string)