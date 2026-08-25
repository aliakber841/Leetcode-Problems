class Solution(object):
    def missingMultiple(self, nums, k):
        hash_table={}
        for i in range(len(nums)):
            hash_table[nums[i]]=i
        j=1
        isFound=False
        while isFound==False:
            k_multiple=k*j
            if k_multiple not in hash_table:
                isFound=True
                return k_multiple  
            j+=1  