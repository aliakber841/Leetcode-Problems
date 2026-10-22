import heapq
class Solution(object):
    def kthLargestNumber(self, nums, k):
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,-int(nums[i]))
        
        for i in range(k-1):
            heapq.heappop(heap)
        result=-heapq.heappop(heap)
        return str(result)