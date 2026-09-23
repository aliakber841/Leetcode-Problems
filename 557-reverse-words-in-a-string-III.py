class Solution(object):
    def reverseWords(self, s):
        list_string=s.split()
        result=[]
        for i in range(0,len(list_string)):
            current_word=list_string[i]
            current_word_list=list(current_word)
            left=0
            right=len(current_word)-1
            while left<=right:
                temp=current_word_list[left]
                current_word_list[left]=current_word_list[right]
                current_word_list[right]=temp
                left+=1
                right-=1
            result.append("".join(current_word_list))
        return " ".join(result)