class Solution(object):
    def destCity(self, paths):
        hash_table={}
        hash_set=set()
        rows=len(paths)
        for i in range(rows):
            hash_table[paths[i][0]]=paths[i][1] 
            hash_set.add(paths[i][0])  
            hash_set.add(paths[i][1])   

        for nums in hash_set:
            if nums not in hash_table: 
                return nums   