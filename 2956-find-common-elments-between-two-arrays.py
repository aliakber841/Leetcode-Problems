class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        hash_set2=set()
        count1=0
        result=[]
        for i in range(len(nums2)):
            hash_set2.add(nums2[i])

        for j in range(len(nums1)):
            if nums1[j] in hash_set2:
                count1+=1
        
        result.append(count1)
        hash_set1=set()
        count2=0

        for i in range(len(nums1)):
            hash_set1.add(nums1[i])

        for j in range(len(nums2)):
            if nums2[j] in hash_set1:
                count2+=1
        
        result.append(count2)
        return result