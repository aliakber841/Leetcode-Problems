class Solution(object):
    def calculate(self, s):
        stack=[]
        result=0
        number=0
        sign=1
        for i in range(len(s)):
            current=s[i]
            if current>="0" and current<="9":
                number=number*10+int(current)
            elif current=="+":
                result=result+sign*number
                number=0
                sign=1
            elif current=="-":
                result=result+sign*number
                number=0
                sign=-1
            elif current=="(":
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1
            elif current==")":
                result=result+sign*number
                number=0
                old_sign=stack.pop()
                old_result=stack.pop()
                result=old_result+old_sign*result
        result=result+sign*number
        return result