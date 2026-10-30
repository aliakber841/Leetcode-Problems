class Solution(object):
    def longestValidParentheses(self, s):
        if len(s)==0:
            return 0
        result=0
        stack=[]
        stack.append(-1)
        for i in range(len(s)):
            current=s[i]
            if current=="(":
                stack.append(i)
            elif current==")":
                stack.pop()
                if stack:
                    length=i-stack[-1]
                    if length>result:
                        result=length
                else:
                    stack.append(i)
        return result