# Kruskal's Algorithm
class Solution(object):
    def minCostConnectPoints(self, points):
        n=len(points)
        parent=[]
        rank=[]
        for i in range(n):
            parent.append(i)
            rank.append(0)
        
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        edges=[]
        for i in range(n):
            for j in range(i+1,n):
                distance=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                edges.append((distance,i,j))
        edges.sort()

        cost=0
        count=0
        for edge in edges:
            distance=edge[0]
            i=edge[1]
            j=edge[2]
            rootI=find(i)
            rootJ=find(j)
            if rootI!=rootJ:
                if rank[rootI]==rank[rootJ]:
                    parent[rootJ]=rootI
                    rank[rootI]+=1
                elif rank[rootI]>rank[rootJ]:
                    parent[rootJ]=rootI
                elif rank[rootI]<rank[rootJ]:
                    parent[rootI]=rootJ
                cost+=distance
                count+=1
                if count==n-1:
                    break
        return cost     

# Prim's Algorithm
import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        n=len(points)
        visited=[]
        for i in range(n):
            visited.append(False)
        
        heap=[(0,0)]
        cost=0
        count=0

        while count<n:
            distance,current=heapq.heappop(heap)
            if visited[i]==True:
                continue
            visited[i]=True
            cost+=distance
            count+=1
            for j in range(n):
                if visited[j]==False:
                    d=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    heapq.heappush(heap,(d,j))
        return cost     