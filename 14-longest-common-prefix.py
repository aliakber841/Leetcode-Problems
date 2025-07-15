class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        first_string=strs[0]
        prefix=""
        for i in range(len(first_string)):
            current_char=first_string[i]
            for s in strs[1:]:
                if i>=len(s) or s[i]!=current_char:
                    return prefix
            prefix+=current_char
        return prefix       
