import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        heap=[]
        if len(stones)==1:
            return stones[0]
        for num in stones:
            heapq.heappush(heap,-num) 
        
        # -8, -7, -4, -2, -1, -1
        while len(heap)>1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)
            if y==x:
                continue
            elif x!=y:
                num=y-x
                heapq.heappush(heap,-num)
        if len(heap)==0:
            return 0
        return -heapq.heappop(heap)  