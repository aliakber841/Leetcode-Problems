import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,-(nums[i]))
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)     