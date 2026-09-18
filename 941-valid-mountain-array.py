class Solution(object):
    def validMountainArray(self, arr):
        if len(arr)<=2:
            return False
        leftValid=False
        rightValid=False
        index=0
        while index+1<len(arr) and arr[index]<arr[index+1]:
            index+=1
            leftValid=True
        while index+1<len(arr) and arr[index]>arr[index+1]:
            index+=1
            rightValid=True 
        return leftValid and rightValid and index==len(arr)-1