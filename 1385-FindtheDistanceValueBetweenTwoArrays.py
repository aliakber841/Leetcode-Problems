class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count=0
        for i in range(len(arr1)):
            target=arr1[i]-d
            high=arr1[i]+d
            left=0
            right=len(arr2)
            while left<right:
                mid=left+(right-left)//2
                if arr2[mid]<target:
                    left=mid+1
                else:
                    right=mid

            is_valid=True
            if left<len(arr2):
                if arr2[left]<=high:
                    is_valid=False
            if is_valid:
                count+=1
        return count

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count=0
        for i in range(len(arr1)):
            isValid=True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    isValid=False
                    break
            if isValid:
                count+=1
        return count