#Union Find
class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        parent=[]
        rank=[]
        for i in range(n):
            parent.append(i)
            rank.append(0)

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        result=n
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    rootI=find(i)
                    rootJ=find(j)
                    if rootI!=rootJ:
                        if rank[rootI]==rank[rootJ]:
                            parent[rootJ]=rootI
                            rank[rootI]+=1
                        elif rank[rootI]<rank[rootJ]:
                            parent[rootI]=rootJ
                        elif rank[rootI]>rank[rootJ]:
                            parent[rootJ]=rootI
                        result-=1
        return result
    
def dfs(isConnected,city,visited):
    visited[city]=True
    for j in range(len(isConnected)):
        if isConnected[city][j]==1 and visited[j]==False:
            dfs(isConnected,j,visited)
class Solution(object):
    def findCircleNum(self, isConnected):
        visited=len(isConnected)*[False]
        result=0
        for i in range(len(isConnected)):
            if visited[i]==False:
                dfs(isConnected,i,visited)
                result+=1
        return result

from collections import deque
class Solution(object):
    def findCircleNum(self, isConnected):
        visited=len(isConnected)*[False]
        result=0
        queue=deque()
        for i in range(len(isConnected)):
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                while queue:
                    city=queue.popleft()
                    for j in range(len(isConnected)):
                        if isConnected[city][j]==1 and visited[j]==False:
                            visited[j]=True
                            queue.append(j)
                result+=1
        return result