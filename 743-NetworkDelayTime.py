import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph=[]
        distance=[]
        for i in range(n+1):
            graph.append([])
            distance.append(float('inf'))
        
        for u,v,w in times:
            graph[u].append((v,w))
        
        distance[k]=0
        heap=[(0,k)]
        #Graph: 2:[(1,1),(3,1)], 3:[(4,1)]
        while heap:
            current_time,current=heapq.heappop(heap)
            if current_time>distance[current]:
                continue
            for neighbour,weight in graph[current]:
                new_time=current_time+weight
                if new_time<distance[neighbour]:
                    distance[neighbour]=new_time
                    heapq.heappush(heap,(new_time,neighbour))
        
        answer=0
        for i in range(1,n+1):
            if distance[i]==float('inf'):
                return -1
            if distance[i]>answer:
                answer=distance[i]
        return answer