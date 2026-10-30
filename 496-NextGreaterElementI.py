class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        hash_table={}
        for i in range(len(nums2)):
            hash_table[nums2[i]]=i

        result=[-1]*len(nums1)
        
        for i in range(len(nums1)):
            index=hash_table[nums1[i]]
            while index+1<len(nums2):
                if nums2[index+1]>nums1[i]:
                    result[i]=nums2[index+1]
                    break
                index+=1
        
        return result