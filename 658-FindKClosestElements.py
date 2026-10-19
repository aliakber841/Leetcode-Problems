class Solution(object):
    def findClosestElements(self, arr, k, x):
        left=0
        right=len(arr)-k
        result=[]
        while left<right:
            mid=left+(right-left)//2

            left_gap=x-arr[mid]
            right_gap=arr[mid+k]-x

            if left_gap>right_gap:
                left=mid+1
            else:
                right=mid

        start=left
        while start<left+k:
            result.append(arr[start])
            start+=1
        return result
        
class Solution(object):
    def findClosestElements(self, arr, k, x):
        left=0
        right=len(arr)-1
        result=[]
        while right-left+1>k:
            if abs(arr[left]-x)<=abs(arr[right]-x):
                right-=1
            else:
                left+=1
                
        while left<=right:
            result.append(arr[left])
            left+=1
        return result