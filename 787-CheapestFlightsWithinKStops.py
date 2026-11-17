import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph=[]
        stops_used=[]
        for i in range(n):
            graph.append([])
            stops_used.append(float('inf'))
        
        for u,v,p in flights:
            graph[u].append((v,p))
        # [
        #     0:1
        #     1:2,3
        #     2:0,3
        # ]
        heap=[]
        heapq.heappush(heap,(0,src,0))
        while heap:
            current_price,current,stops=heapq.heappop(heap)
            if current==dst:
                return current_price
            if stops>k:
                continue
            if stops>=stops_used[current]:
                continue
            stops_used[current]=stops
            for neighbours,pr in graph[current]:
                new_price=current_price+pr
                heapq.heappush(heap,(new_price,neighbours,stops+1))
        return -1