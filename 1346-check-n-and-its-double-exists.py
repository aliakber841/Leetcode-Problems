class Solution(object):
    def checkIfExist(self, arr):
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if i!=j:
                    if arr[i]==arr[j]*2:
                        return True
        return False     

class Solution(object):
    def checkIfExist(self, arr):
        hash_table={}
        for i in range(0,len(arr)):
            if arr[i] not in hash_table:
                hash_table[arr[i]]=1
            else:
                hash_table[arr[i]]+=1

        for i in range(0,len(arr)):
            target=arr[i]*2
            if target in hash_table:
                if target!=arr[i]:
                    return True
                elif hash_table[arr[i]]>1:
                    return True
        return False     