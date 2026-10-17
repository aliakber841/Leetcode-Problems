class Solution(object):
    def isIsomorphic(self, s, t):
        hash_table={}
        for i in range(len(s)):
            if s[i] in hash_table:
                continue
            else:
                hash_table[s[i]]=t[i]
         
        for j in range(len(t)):
            if t[j]!=hash_table[s[j]]:
                return False
        
        seen=set()
        for letter in hash_table:
            mapped=hash_table[letter]
            if mapped in seen:
                return False
            seen.add(mapped)
        return True