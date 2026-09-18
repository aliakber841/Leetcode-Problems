class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Checking from right which element is greater from an array
        # Append that to end of nums1 and decrement the length
        nums1_length=(m+n)-1 
        i=m-1 
        j=n-1 
        while j>=0:
            if i>=0 and nums1[i]>=nums2[j]:
                nums1[nums1_length]=nums1[i]
                i-=1
            else:
                nums1[nums1_length]=nums2[j]
                j-=1
            nums1_length-=1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n==0:
            return
        index=0
        for i in range(m,len(nums1)):
            nums1[i]=nums2[index]
            index+=1
        nums1.sort()