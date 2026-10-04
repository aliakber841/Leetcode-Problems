class Solution(object):
    def interpret(self, command):
        result=""
        stack=[]
        for i in range(len(command)):
            if command[i]=="G":
                result+=command[i]
            elif command[i]=="(" or command[i]=="a" or command[i]=="l":
                stack.append(command[i])
            elif command[i]==")":
                top=stack.pop()
                if top=="(":
                    result+="o"
                elif top=="l":
                    stack.pop()
                    stack.pop()
                    result+="al"    
        return result

class Solution(object):
    def interpret(self, command):
        return command.replace("()","o").replace("(al)","al")