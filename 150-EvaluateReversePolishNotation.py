# Postfix Notation
class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        result=0
        for i in range(len(tokens)):
            current=tokens[i]
            if current!="+" and current!="-" and current!="*" and current!="/":
                result=int(current)
                stack.append(result)
                result=0
            elif current=="+" or current=="-" or current=="*" or current=="/":
                if current=="+":
                    num1=stack.pop()
                    num2=stack.pop()
                    result=num1+num2
                    stack.append(result)
                elif current=="-":
                    num1=stack.pop()
                    num2=stack.pop()
                    result=num2-num1
                    stack.append(result)
                elif current=="*":
                    num1=stack.pop()
                    num2=stack.pop()
                    result=num1*num2
                    stack.append(result)
                elif current=="/":
                    num2=stack.pop()
                    num1=stack.pop()
                    result=int(float(num1)/num2)
                    stack.append(result)
                result=0
        return stack[-1]