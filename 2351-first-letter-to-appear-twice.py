# Set (Unordered set)
class Solution(object):
    def repeatedCharacter(self, s):
        current=set()
        for i in s:
            if i in current:
                return i
            current.add(i)
        return ""

# Hash Table (Unordered Map)
class Solution(object):
    def repeatedCharacter(self, s):
        hash_table={}
        first_twice=""
        for i in range(len(s)):
            if s[i] in hash_table:
                hash_table[s[i]].append(i)
            else:
                 hash_table[s[i]]=[i]
        for j in hash_table:
            if len(hash_table[j])>=2:
                if not first_twice:
                    first_twice=j
                else:
                    if hash_table[j][1]<hash_table[first_twice][1]:
                        first_twice=j
        return first_twice   