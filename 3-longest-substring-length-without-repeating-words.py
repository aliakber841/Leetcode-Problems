class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        current_string=''
        previous_string=''
        for i in range(len(s)):
            if s[i] not in current_string:
                current_string+=s[i]
            else:
                if len(current_string)>len(previous_string):
                    previous_string=current_string
                duplicate_char_index=current_string.index(s[i])
                current_string=current_string[duplicate_char_index+1:]+s[i]
        return max(len(previous_string),len(current_string))