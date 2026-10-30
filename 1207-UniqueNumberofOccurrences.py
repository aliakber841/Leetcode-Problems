class Solution(object):
    def uniqueOccurrences(self, arr):
        hash_table={}
        for i in range(len(arr)):
            if arr[i] not in hash_table:
                hash_table[arr[i]]=1
            else:
                hash_table[arr[i]]+=1
        
        seen=set()
        for key,value in hash_table.items():
            if value in seen:
                return False
            seen.add(value)
        
        return True