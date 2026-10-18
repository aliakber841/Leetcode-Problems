import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.k=k
        self.pq=[]

        for num in nums:
            if len(self.pq)<k:
                heapq.heappush(self.pq, num)
            else:
                heapq.heappush(self.pq, num)
                heapq.heappop(self.pq)
        

    def add(self, val):
        if len(self.pq)<self.k:
            heapq.heappush(self.pq, val)
        else:
            heapq.heappush(self.pq, val)
            heapq.heappop(self.pq)

        return self.pq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)