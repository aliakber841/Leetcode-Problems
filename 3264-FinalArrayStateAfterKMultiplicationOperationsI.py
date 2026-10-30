import heapq
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))
        
        while k>0:
            number1,index1=heapq.heappop(heap)
            nums[index1]=number1*multiplier
            heapq.heappush(heap,(nums[index1],index1))
            k-=1
           
        return nums