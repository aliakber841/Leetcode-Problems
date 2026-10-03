class Solution(object):
    def restoreString(self, s, indices):
        list_string=list(s)
        for i in range(len(s)): 
            position=indices[i] 
            list_string[position]=s[i] 
        return "".join(list_string)  