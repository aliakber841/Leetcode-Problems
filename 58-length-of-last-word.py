class Solution(object):
    def lengthOfLastWord(self, s):
        list_of_string=s.split()
        total_index=len(list_of_string)-1
        last_index_value=list_of_string[total_index]
        return len(last_index_value)