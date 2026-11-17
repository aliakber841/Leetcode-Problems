class Solution(object):
    def minSubArrayLen(self, target, nums):
        prefixSum=nums[:]
        for i in range(1,len(prefixSum)):
            prefixSum[i]=prefixSum[i-1]+nums[i]
        
        left=0
        min_size=0
        #[2,5,6,8,12,15]
        for i in range(len(nums)):
            if prefixSum[i]<target:
                continue
            if left==0:
                window_sum=prefixSum[i]
            else:
                window_sum=prefixSum[i]-prefixSum[left-1]
            while window_sum>=target:
                window_length=i-left+1
                if min_size==0:
                    min_size=window_length
                elif window_length<min_size:
                    min_size=window_length
                left+=1
                window_sum=prefixSum[i]-prefixSum[left-1] 
        return min_size
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        sum_digits=0
        count=0
        for i in range(len(nums)):
           sum_digits+=nums[i]
           while sum_digits>=target:
            window_length=i-left+1
            if count==0:
                count=window_length
            elif window_length<count:
                count=window_length
            sum_digits-=nums[left]
            left+=1
        return count