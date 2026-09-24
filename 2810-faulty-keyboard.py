# Optimal
class Solution(object):
    def finalString(self, s):
        result=[]
        list_string=list(s)
        reverse=False
        for i in range(len(list_string)):
            current_char=list_string[i]
            if current_char=="i":
                reverse=not reverse
            else:
                if reverse:
                    result.insert(0,current_char)
                else:
                    result.append(current_char)
        if reverse:
            result.reverse()
        return "".join(result)

class Solution(object):
    def finalString(self, s):
        result=[]
        list_string=list(s)
        for i in range(len(list_string)):
            if list_string[i]=="i":
                left=0
                right=i
                while left<right:
                    temp=list_string[left]
                    list_string[left]=list_string[right]
                    list_string[right]=temp
                    left+=1
                    right-=1
        
        for i in range(0,len(list_string)):
            if list_string[i]!="i":
                result.append(list_string[i])

        return "".join(result)