class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in range(len(s)):
            if stack and s[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return "".join(stack)
    
class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        previous=""
        current=""
        for i in range(len(s)):
            current=s[i]
            if len(stack)>=1 and previous==current:
                stack.pop()
                if len(stack)>=1:
                    previous=stack[-1]
                else:
                    previous=""
            else:
                stack.append(s[i])
                previous=current
        
        return "".join(stack)