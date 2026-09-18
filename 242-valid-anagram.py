class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        hash_table={}
        for i in range(len(s)):
            if s[i] not in hash_table:
                hash_table[s[i]]=1
            else:
                 hash_table[s[i]]+=1
        
        for i in range(len(t)):
            if t[i] in hash_table and hash_table[t[i]]>=1:
                hash_table[t[i]]-=1
            else:
                return False
        return True