class Solution(object):
    def romanToInt(self, s):
        int_number=0
        roman_values={
            'I':1,
            'V':5,
            'X':10,
           'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        for i in range(0,len(s)):
           current_value=roman_values[s[i]]
           int_number+=current_value
           if i>0:
            previous_value=roman_values[s[i-1]]
            if previous_value<current_value:
                int_number-=2*previous_value
        return int_number
# class Solution(object):
#     def romanToInt(self, s):
#         str_number=0
#         for i in range(0,len(s)):
#             if s[i]=='I':
#                 str_number+=1
#             if s[i]=='V':
#                 if i>0 and s[i-1]=='I':
#                  str_number+=3
#                 else:
#                  str_number+=5
#             if s[i]=='X':
#                 if i>0 and s[i-1]=='I':
#                  str_number+=8
#                 else:
#                  str_number+=10
#             if s[i]=='L':
#                 if i>0 and s[i-1]=='X':
#                  str_number+=30
#                 else:
#                  str_number+=50
#             if s[i]=='C':
#                 if i>0 and s[i-1]=='X':
#                  str_number+=80
#                 else:
#                  str_number+=100
#             if s[i]=='D':
#                 if i>0 and s[i-1]=='C':
#                  str_number+=300
#                 else:
#                  str_number+=500
#             if s[i]=='M':
#                 if i>0 and s[i-1]=='C':
#                  str_number+=800
#                 else:
#                  str_number+=1000
#         return str_number

        
        