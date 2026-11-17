from collections import deque
class Solution(object):
    def getAncestors(self, n, edges):
        graph=[]
        indegree=[]
        result=[]
        for i in range(n):
            indegree.append(0)
            graph.append([])
            result.append([])
        
        for a,b in edges:
            indegree[b]+=1
            graph[a].append(b)
        
        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            current=queue.popleft()
            for neighbours in graph[current]:
                indegree[neighbours]-=1
                result[neighbours].append(current)
                i=0
                while i<len(result[current]):
                    value=result[current][i]
                    if value not in result[neighbours]:
                        result[neighbours].append(value)
                    i+=1
                if indegree[neighbours]==0:
                    queue.append(neighbours)
        for i in range(n):
            result[i].sort()
        return result