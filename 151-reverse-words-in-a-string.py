class Solution(object):
    def reverseWords(self, s):
        string_list=s.split(" ")
        result=[]
        for i in range(len(string_list)-1,-1,-1):
            if string_list[i]!="":
                result.append(string_list[i])
        return " ".join(result)