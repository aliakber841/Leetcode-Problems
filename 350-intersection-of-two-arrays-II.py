class Solution(object):
    def intersect(self, nums1, nums2):
        result=[]
        hash_table={}
        for i in range(len(nums1)):
            if nums1[i] in hash_table:
                hash_table[nums1[i]]+=1
            else:
                hash_table[nums1[i]]=1
        for j in range(len(nums2)):
            if nums2[j] in hash_table and hash_table[nums2[j]]>0:
                result.append(nums2[j])
                hash_table[nums2[j]]-=1
        return result

# Optimal Approach
def hash_map(nums,hash_table):
    for i in range(len(nums)):
            if nums[i] in hash_table:
                hash_table[nums[i]]+=1
            else:
                hash_table[nums[i]]=1

def intersection(nums,hash_table,result):
    for j in range(len(nums)):
        if nums[j] in hash_table and hash_table[nums[j]]>0:
            result.append(nums[j])
            hash_table[nums[j]]-=1
                
class Solution(object):
    def intersect(self, nums1, nums2):
        result=[]
        hash_table={}
        if len(nums1)<=len(nums2):
            hash_map(nums1,hash_table)
            intersection(nums2,hash_table,result) 
        else:
            hash_map(nums2,hash_table)
            intersection(nums1,hash_table,result)
        return result