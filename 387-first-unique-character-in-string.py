class Solution(object):
    def firstUniqChar(self, s):
        hash_table={}
        for i in range(len(s)):
             if s[i] in hash_table:
                hash_table[s[i]]+=1
             else:
                hash_table[s[i]]=1
        for j in range(len(s)):
            if hash_table[s[j]]==1:
                return j  
        return -1