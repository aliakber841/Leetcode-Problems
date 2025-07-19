class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if len(haystack)<len(needle):
            return -1
        current_string=""
        needle_length=len(needle)
        for i in range(len(haystack)):
            current_string+=haystack[i]
            if len(current_string)>needle_length:
                current_string=current_string[-needle_length:]
            if current_string==needle:
                return i-needle_length+1
        return -1 