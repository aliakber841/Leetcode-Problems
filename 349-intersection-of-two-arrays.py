class Solution(object):
    def intersection(self, nums1, nums2):
        result=[]
        hash_table={}
        for i in range(len(nums1)):
            if nums1[i] not in hash_table:
                hash_table[nums1[i]]=True
        for j in range(len(nums2)):
            if nums2[j] in hash_table:
                result.append(nums2[j])
                del hash_table[nums2[j]]
        return result