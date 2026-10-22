class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)

        mid=n//2
        
        if n%2!=0:
            return nums1[mid]
        else:
            return (nums1[mid-1]+nums1[mid])/2.0
            
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1=len(nums1)
        len2=len(nums2)
        i=0
        j=0
        total=len1+len2
        n=total//2
        count=n+1
        val1=0
        val2=0
        while count>0:
            val1=val2
            if i<len1 and j<len2:
                if nums1[i]<=nums2[j]:
                    val2=nums1[i]
                    i+=1
                else:
                    val2=nums2[j]
                    j+=1
            elif i<len1:
                val2=nums1[i]
                i+=1
            else:
                val2=nums2[j]
                j+=1
            count-=1
        if total%2!=0:
            return val2
        else:
            return (val1+val2)/2.0