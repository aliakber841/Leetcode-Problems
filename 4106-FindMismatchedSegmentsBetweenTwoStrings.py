class Solution(object):
    def findMismatchedSegments(self, s1, s2):
        str1=""
        str2=""
        result=[]
        for i in range(len(s1)):  
            if s1[i]!=s2[i]:
                str1+=s1[i]
                str2+=s2[i]
            elif s1[i]==s2[i]:
                if str1!="":
                    current=[]
                    current.append(str1)
                    current.append(str2)
                    result.append(current)
                    str1=""
                    str2=""

        if str1!="":
            current=[]
            current.append(str1)
            current.append(str2)
            result.append(current)
            
        return result   