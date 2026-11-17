#Bellman Ford Algorithm
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        threshold=[]
        for i in range(n):
            threshold.append([])
        
        for i in range(n):
            distance=[]
            for j in range(n):
                distance.append(float('inf'))
            
            distance[i]=0
            for step in range(n-1):
                changed=False
                for u,v,w in edges:
                    new_distance=distance[u]+w
                    if new_distance<distance[v]:
                        distance[v]=new_distance
                        changed=True
                    new_distance=distance[v]+w
                    if new_distance<distance[u]:
                        distance[u]=new_distance
                        changed=True
                if not changed:
                    break
            
            for j in range(n):
                if i!=j and distance[j]<=distanceThreshold:
                    threshold[i].append(j)                   
        
        length=float('inf')
        answer=0
        for i in range(n):
            if len(threshold[i])<=length:
                length=len(threshold[i])
                answer=i
        return answer
            # [
            #     0:1
            #     1:0,2,3
            #     2:1,3
            #     3:1,2
            # ]     

#Dijkstra Algorithm
import heapq
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        graph=[]
        threshold=[]
        for i in range(n):
            graph.append([])
            threshold.append([])
        
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        for i in range(n):
            distance=[]
            for j in range(n):
                distance.append(float('inf'))
            distance[i]=0
            heap=[(0,i)]
            while heap:
                current_distance,current=heapq.heappop(heap)
                if current_distance>distance[current]:
                    continue
                for neighbours,wt in graph[current]:
                    new_distance=current_distance+wt
                    if new_distance>distanceThreshold:
                        continue
                    elif new_distance<distance[neighbours]:
                        distance[neighbours]=new_distance
                        heapq.heappush(heap,(new_distance,neighbours))
            
            for j in range(n):
                if i!=j and distance[j]<=distanceThreshold:
                    threshold[i].append(j)                   
        
        length=float('inf')
        answer=0
        for i in range(n):
            if len(threshold[i])<=length:
                length=len(threshold[i])
                answer=i
        return answer
            # [
            #     0:1
            #     1:0,2,3
            #     2:1,3
            #     3:1,2
            # ]     