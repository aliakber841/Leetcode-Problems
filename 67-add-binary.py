class Solution(object):
    def addBinary(self, a, b):
        result=[]
        carry=''
        a_last=len(a)-1
        b_last=len(b)-1
        while a_last>=0 or b_last>=0:
            current_a=a[a_last] if a_last>=0 else '0'  
            current_b=b[b_last] if b_last>=0 else '0'  
            if current_a=='0' and current_b=='0':
                if carry=='':
                    result.append('0')
                else:
                    result.append('1')
                    carry=''
            elif (current_a=='0' and current_b=='1') or (current_a=='1' and current_b=='0'):
                if carry=='':
                    result.append('1')
                else:
                    result.append('0')
                    carry='1'
            elif current_a=='1' and current_b=='1':
                if carry=='':
                    result.append('0')
                    carry='1'
                else:
                    result.append('1')
                    carry='1'
            a_last-=1
            b_last-=1
        if carry:
                result.append(carry)
        reverse_string=''.join(reversed(result))
        return reverse_string 
