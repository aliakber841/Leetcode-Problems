class Solution(object):
    def countConsistentStrings(self, allowed, words):
        hash_table={}
        count=0
        for i in range(len(allowed)):
            hash_table[allowed[i]]=i
        
        for i in range(len(words)):
            current_word=words[i]
            isValid=True
            for j in range(len(current_word)):
                if current_word[j] not in hash_table:
                    isValid=False
                    break
            if isValid:
                count+=1
        return count

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set=set(allowed)
        count=0
        
        for i in range(len(words)):
            current_word=words[i]
            isValid=True
            for j in range(len(current_word)):
                if current_word[j] not in allowed_set:
                    isValid=False
                    break
            if isValid:
                count+=1
        return count