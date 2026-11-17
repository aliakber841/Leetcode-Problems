class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        set1=set()
        for i in range(len(nums1)):
            set1.add(nums1[i])
        
        set2=set()
        for i in range(len(nums2)):
            set2.add(nums2[i])
        
        set3=set()
        for i in range(len(nums3)):
            set3.add(nums3[i])
        
        resultSet=set()
        for key in set1:
            if key in set2:
                resultSet.add(key)
        
        for key in set1:
            if key in set3:
                resultSet.add(key)
        
        for key in set2:
            if key in set3:
                resultSet.add(key)
        
        return list(resultSet)