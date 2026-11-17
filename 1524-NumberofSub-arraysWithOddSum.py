class Solution(object):
    def numOfSubarrays(self, arr):
        result=0
        prefixSum=arr[:]
        for i in range(1,len(arr)):
            prefixSum[i]=prefixSum[i-1]+arr[i]
        odd=0
        even=1
        for i in range(len(arr)):
            if prefixSum[i]%2==1:
                result+=even
                odd+=1
            else:
                result+=odd
                even+=1
        return result%(10**9+7)