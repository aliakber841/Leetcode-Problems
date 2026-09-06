# Reverse Approach
def reverse_array(arr,left,right):
        while left<=right:
            temp=arr[left]
            arr[left]=arr[right]
            arr[right]=temp
            left+=1
            right-=1
class Solution(object):
    def rotate(self, nums, k):
        arr_length=len(nums)
        if k%arr_length==0:
            return
        k=k%arr_length 
        reverse_array(nums,0,arr_length-1) 
        reverse_array(nums,0,k-1)   
        reverse_array(nums,k,arr_length-1)   
        return nums    

# Cyclic Replacement Approach (Permutation Cycle)
class Solution(object):
    def rotate(self, nums, k):
        arr_length=len(nums)
        k=k%arr_length
        if k==0:
            return
        count=0
        start=0
        while count<arr_length:
            current_index=start
            prev=nums[start]
            while True:
                rotate_index=(current_index+k)%arr_length 

                temp=nums[rotate_index]
                nums[rotate_index]=prev
                prev=temp
                
                current_index=rotate_index
                count+=1
                if current_index==start:
                    break
            start+=1
        return nums