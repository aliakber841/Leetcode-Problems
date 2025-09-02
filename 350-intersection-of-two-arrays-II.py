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