def merge(nums,start,mid,end):
    left=nums[start:mid+1]
    right=nums[mid+1:end+1]

    i=0
    j=0
    k=start

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
        k+=1
    
    while i<len(left): #if right completes fill left subarray all elmeents
        nums[k]=left[i]
        i+=1
        k+=1
    
    while j<len(right): #if left completes fill right subarray all elmeents
        nums[k]=right[j]
        j+=1
        k+=1

def mergeSort(nums,start,end):
    if start<end:
        mid=start+(end-start)//2

        mergeSort(nums,start,mid) #left subtree
        mergeSort(nums,mid+1,end) #right subtree

        merge(nums,start,mid,end) # sort left and right subtree
class Solution(object):
    def thirdMax(self, nums):
        mergeSort(nums,0,len(nums)-1)

        count=1
        maxNumber=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]==maxNumber:
                continue
            maxNumber=nums[i]
            count+=1
            if count==3:
                return maxNumber
        return nums[-1]