class Solution(object):
    def duplicateZeros(self, arr):
        n=len(arr)-1
        count_zeroes=0
        i=0
        while i<=n-count_zeroes:
            if arr[i]==0:
                if i==n-count_zeroes:
                    arr[n]=0
                    n-=1
                    break
                count_zeroes+=1
            i+=1
                
        
        newIndex=n-count_zeroes
        while newIndex>=0:
            if arr[newIndex]==0:
                arr[newIndex+count_zeroes]=0
                count_zeroes-=1
                arr[newIndex+count_zeroes]=0
            else:
                arr[newIndex+count_zeroes]=arr[newIndex]
            newIndex-=1