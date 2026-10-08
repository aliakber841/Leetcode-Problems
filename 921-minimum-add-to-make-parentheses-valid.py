# # Take two variables open_bracket and close_brackets.
# If "(" comes, always increment open_bracket (it is waiting for a ")").
# If ")" comes and open_bracket>0, both brackets match, so decrement open_bracket by 1.
# If ")" comes and open_bracket==0, there is nothing to match, so increment close_brackets.
# At the end, open_bracket = unmatched "(" (each needs a ")" inserted), close_brackets = unmatched ")" (each needs a "(" inserted).
# Return open_bracket+close_brackets
class Solution(object):
    def minAddToMakeValid(self, s):
        open_bracket=0
        close_bracket=0
        for i in range(len(s)):
            if s[i]=="(":
                open_bracket+=1
            else:
                if open_bracket>0:
                    open_bracket-=1
                else:
                    close_bracket+=1
        return open_bracket+close_bracket