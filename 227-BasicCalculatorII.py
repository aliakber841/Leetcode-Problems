class Solution(object):
    def calculate(self, s):
        s=s.replace(" ","")
        result=0
        sign="+"
        stack=[]
        number=0
        for i in range(len(s)):
            current=s[i]
            if current>="0" and current<="9":
                number=number*10+int(current)
            if current=="+" or current=="-" or current=="*" or current=="/" or i==len(s)-1:
                if sign=="+":
                    stack.append(number)
                elif sign=="-":
                    stack.append(-number)
                elif sign=="*":
                    num=stack.pop()
                    stack.append(num*number)
                elif sign=="/":
                    num=stack.pop()
                    stack.append(int(float(num)/number))
                sign=current
                number=0

        while stack:
            result+=stack.pop()
        return result