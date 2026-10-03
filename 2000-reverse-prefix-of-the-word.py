class Solution(object):
    def reversePrefix(self, word, ch):
        list_string=list(word)
        right=-1
        for i in range(len(list_string)):
            if list_string[i]==ch:
                right=i
                break

        if right==-1:
            return word
        
        left=0
        while left<right:
            temp=list_string[left]
            list_string[left]=list_string[right]
            list_string[right]=temp

            left+=1
            right-=1
        return "".join(list_string)