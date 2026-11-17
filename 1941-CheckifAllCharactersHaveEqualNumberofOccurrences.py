class Solution(object):
    def areOccurrencesEqual(self, s):
        hash_table={}
        for i in range(len(s)):
            if s[i] in hash_table:
                hash_table[s[i]]+=1
            else:
                hash_table[s[i]]=1
        
        array=[]
        for key,value in hash_table.items():
            array.append(value)
        
        frequency=array[0]
        for i in range(1,len(array)):
            if array[i]!=frequency:
                return False
        return True