# Whitespaces at start should be ignored. If these comes after a digit (1-9) then we have to return the result
# + and -: both are allowed only once,right after the leading spaces.A second sign ("+-12","-+12") stops the reading and gives 0
# Negative Sign is only added to the result if it comes at start of string (ist time). If it comes after the digit>(1-9), return the result
# Ignore all zeroes if it comes at start of string. If the string start with a digit>(1-9) then the zeroes comes, it can be added to result
# If digit>(1-9) comes simply append it to the result. If a non digit comes (letter, "."), stop and return the result. If no digits are read, return 0
# Clamp to -2147483648 ... 2147483647
class Solution(object):
    def myAtoi(self, s):
        string=list(s)
        result=[]
        i=0
        sign=1
        # Handle Leading WhiteSpaces
        while i<len(string) and string[i]==" ":
            i+=1
        # Handle "+:-" Sign
        if i<len(string) and (string[i]=="+" or string[i]=="-"):
            if string[i]=="-":
                sign=-1
            i+=1
        # Handle Conversion
        while i<len(string):
            if string[i].isdigit()==True:
                result.append(string[i])
                i+=1
            else:
                break
        
        number=0
#ord(...) gives the character's code number. ord("0") is 48, ord("1") is 49, ..., ord("9") is 57.
# So ord('4')-ord("0") is 52-48 = 4. The subtraction turns the character into its real digit value.
# number*10+digit moves the old digits one place left and adds the new digit.
        for i in range(len(result)):
            digit=ord(result[i])-ord("0")
            number=number*10+digit

        number=number*sign
            
        # Handle Rounding
        if number>2**31-1:
            return 2**31-1
        if number<-2**31:
            return -2**31
        return number