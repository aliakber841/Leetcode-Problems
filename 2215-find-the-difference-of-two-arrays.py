class Solution(object):
    def findDifference(self, nums1, nums2):
        set1=set(nums1)
        set2=set(nums2)

        answer1=list(set1-set2)
        answer2=list(set2-set1)

        return [answer1,answer2]

class Solution(object):
    def findDifference(self, nums1, nums2):
        result=[]
        hash_set2=set()
        list1=[]
        seen1=set()
        for i in range(len(nums2)):
            hash_set2.add(nums2[i])

        for j in range(len(nums1)):
            if nums1[j] not in hash_set2:
                if nums1[j] in seen1:
                    continue
                else:
                    list1.append(nums1[j])
                    seen1.add(nums1[j])
        
        result.append(list1)
        hash_set1=set()
        list2=[]
        seen2=set()

        for i in range(len(nums1)):
            hash_set1.add(nums1[i])

        for j in range(len(nums2)):
            if nums2[j] not in hash_set1:
                if nums2[j] in seen2:
                    continue
                else:
                    list2.append(nums2[j])
                    seen2.add(nums2[j])
        
        result.append(list2)
        return result

class Solution(object):
    def findDifference(self, nums1, nums2):
        hash_set1=set()
        hash_set2=set()

        for i in range(len(nums1)):
            hash_set1.add(nums1[i])

        for i in range(len(nums2)):
            hash_set2.add(nums2[i])

        list1=[]
        for value in hash_set1:
            if value not in hash_set2:
                list1.append(value)

        list2=[]
        for value in hash_set2:
            if value not in hash_set1:
                list2.append(value)

        return [list1,list2]