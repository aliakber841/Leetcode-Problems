class Solution(object):
    def replaceElements(self, arr):
        greatest=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=greatest
            if current>greatest:
                greatest=current
        return arr